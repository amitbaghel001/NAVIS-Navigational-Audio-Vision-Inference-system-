import pyttsx3
import speech_recognition as sr
import threading
import queue
import time
import subprocess
import re
from typing import Optional, Callable, Dict, List
from loguru import logger
from dataclasses import dataclass
from enum import Enum
from functools import total_ordering

class AudioPriority(Enum):
    LOW = 1
    NORMAL = 2
    HIGH = 3
    EMERGENCY = 4

@total_ordering
@dataclass
class AudioMessage:
    text: str
    priority: AudioPriority
    timestamp: float
    callback: Optional[Callable] = None
    
    def __lt__(self, other):
        if not isinstance(other, AudioMessage):
            return NotImplemented
        if self.priority.value != other.priority.value:
            return self.priority.value < other.priority.value
        return self.timestamp < other.timestamp
    
    def __eq__(self, other):
        if not isinstance(other, AudioMessage):
            return NotImplemented
        return (self.priority.value == other.priority.value and 
                self.timestamp == other.timestamp)

class SmartVoiceCommandProcessor:
    """Advanced voice command processor with pattern matching and context awareness"""
    
    def __init__(self):
        self.command_patterns = {
            # Scene description commands
            'describe_scene': [
                r'what do you see',
                r'describe scene',
                r'tell me what\'s here',
                r'what\'s in front of me',
                r'what\'s around me',
                r'describe surroundings',
                r'what\'s there',
                r'what can you see',
                r'describe what\'s here',
                r'tell me about the scene',
                r'what objects are here',
                r'what\'s nearby',
                r'scan the area',
                r'look around',
                r'what\'s present',
                r'identify objects',
                r'what am i looking at',
                r'analyze scene',
                r'what\'s visible',
                r'give me details'
            ],
            
            # Navigation commands
            'repeat_last': [
                r'repeat',
                r'say again',
                r'say that again',
                r'repeat last',
                r'what did you say',
                r'could you repeat',
                r'pardon',
                r'excuse me',
                r'i didn\'t catch that',
                r'come again',
                r'repeat that',
                r'say it again',
                r'one more time',
                r'didn\'t hear you',
                r'missed that'
            ],
            
            # Control commands
            'stop_talking': [
                r'stop talking',
                r'be quiet',
                r'silence',
                r'shut up',
                r'stop speaking',
                r'mute',
                r'quiet',
                r'hush',
                r'stop',
                r'enough',
                r'pause',
                r'stop now',
                r'be silent',
                r'no more',
                r'that\'s enough'
            ],
            
            # Emergency commands
            'emergency': [
                r'help me',
                r'emergency',
                r'call for help',
                r'get help',
                r'i need help',
                r'assistance',
                r'urgent',
                r'crisis',
                r'emergency help',
                r'call emergency',
                r'need assistance',
                r'help please',
                r'emergency situation',
                r'urgent help',
                r'immediate help',
                r'panic',
                r'danger',
                r'trouble',
                r'call someone',
                r'get someone'
            ],
            
            # Location commands
            'get_location': [
                r'where am i',
                r'what\'s my location',
                r'where is this',
                r'current location',
                r'my position',
                r'where are we',
                r'what place is this',
                r'location please',
                r'tell me location',
                r'find my location',
                r'gps location',
                r'coordinates',
                r'address',
                r'what\'s the address',
                r'where exactly am i'
            ],
            
            # Audio control commands
            'volume_up': [
                r'volume up',
                r'louder',
                r'increase volume',
                r'turn up',
                r'speak louder',
                r'higher volume',
                r'boost volume',
                r'make it louder',
                r'turn volume up',
                r'increase sound',
                r'more volume',
                r'amplify'
            ],
            
            'volume_down': [
                r'volume down',
                r'quieter',
                r'decrease volume',
                r'turn down',
                r'speak quieter',
                r'lower volume',
                r'reduce volume',
                r'make it quieter',
                r'turn volume down',
                r'decrease sound',
                r'less volume',
                r'softer'
            ],
            
            'speed_up': [
                r'speak faster',
                r'speed up',
                r'talk faster',
                r'faster speech',
                r'increase speed',
                r'talk quickly',
                r'speak quickly',
                r'more speed',
                r'accelerate speech',
                r'quick speech'
            ],
            
            'slow_down': [
                r'speak slower',
                r'slow down',
                r'talk slower',
                r'slower speech',
                r'decrease speed',
                r'talk slowly',
                r'speak slowly',
                r'less speed',
                r'decelerate speech',
                r'slow speech'
            ],
            
            # Calibration commands
            'calibrate': [
                r'calibrate',
                r'calibration',
                r'adjust distance',
                r'fix distance',
                r'calibrate distance',
                r'distance calibration',
                r'adjust measurements',
                r'fix measurements',
                r'tune distance',
                r'correct distance',
                r'set distance',
                r'configure distance',
                r'distance setup',
                r'measurement setup'
            ],
            
            # System commands
            'status': [
                r'system status',
                r'how are you',
                r'status report',
                r'check status',
                r'system check',
                r'health check',
                r'are you working',
                r'system info',
                r'diagnostic',
                r'report status',
                r'how\'s the system',
                r'everything ok',
                r'system report',
                r'check system'
            ]
        }
        
        # Compile regex patterns for faster matching
        self.compiled_patterns = {}
        for command, patterns in self.command_patterns.items():
            self.compiled_patterns[command] = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    
    def process_command(self, text: str) -> str:
        """Process voice command using pattern matching"""
        if not text:
            return "unknown"
        
        text = text.strip().lower()
        
        # Check each command pattern
        for command, patterns in self.compiled_patterns.items():
            for pattern in patterns:
                if pattern.search(text):
                    logger.info(f"Matched command '{command}' from text: '{text}'")
                    return command
        
        logger.info(f"No command pattern matched for: '{text}'")
        return "unknown"

class AudioProcessor:
    def __init__(self):
        """Initialize enhanced audio processing system"""
        self.tts_engine = None
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Enhanced recognition settings
        self._configure_recognizer()
        
        # Audio queues
        self.speech_queue = queue.Queue()
        self.is_speaking = False
        self.audio_thread = None
        
        # State
        self.running = False
        self.voice_commands_enabled = True
        
        # Smart command processor
        self.command_processor = SmartVoiceCommandProcessor()
        
        # Voice command lock to prevent concurrent listening
        self._listening_lock = threading.Lock()
        self._is_listening = False
        
        # Initialize components
        self._initialize_tts()
        self._initialize_speech_recognition()
        
        logger.info("Enhanced audio processor initialized")
    
    def _configure_recognizer(self):
        """Configure speech recognizer with optimal settings"""
        # Adjust for ambient noise and detection sensitivity
        self.recognizer.energy_threshold = 300  # Adjust based on environment
        self.recognizer.pause_threshold = 0.8   # Seconds of silence to mark the end
        self.recognizer.dynamic_energy_adjustment = True
        self.recognizer.dynamic_energy_ratio = 1.5
        self.recognizer.non_speaking_duration = 0.5
    
    def _initialize_tts(self):
        """Initialize text-to-speech engine"""
        try:
            self.tts_engine = pyttsx3.init()
            
            # Configure voice properties
            voices = self.tts_engine.getProperty('voices')
            if voices:
                voice_index = min(1, len(voices) - 1)
                self.tts_engine.setProperty('voice', voices[voice_index].id)
            
            self.tts_engine.setProperty('rate', 160)  # Slightly faster
            self.tts_engine.setProperty('volume', 1.0)
            
            logger.info("TTS engine initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize TTS: {e}")
            raise
    
    def _initialize_speech_recognition(self):
        """Initialize speech recognition with optimal settings"""
        try:
            # Test microphone and adjust for ambient noise
            with self.microphone as source:
                logger.info("Calibrating microphone for optimal recognition...")
                self.recognizer.adjust_for_ambient_noise(source, duration=2)
                
            logger.info(f"Speech recognition initialized - Energy threshold: {self.recognizer.energy_threshold}")
            
        except Exception as e:
            logger.error(f"Failed to initialize speech recognition: {e}")
    
    def speak_async(self, text: str, priority: AudioPriority = AudioPriority.NORMAL,
                   callback: Optional[Callable] = None):
        """Add text to speech queue for asynchronous playback"""
        if not text or text.strip() == "." or text.strip() == "":
            return
        
        message = AudioMessage(
            text=text,
            priority=priority,
            timestamp=time.time(),
            callback=callback
        )
        
        self.speech_queue.put(message)
    
    def speak_immediately(self, text: str, interrupt: bool = False):
        """Speak text immediately using Windows SAPI"""
        if not text or text.strip() == "." or text.strip() == "":
            return
        
        try:
            if interrupt:
                self.stop_speaking()
            
            self.is_speaking = True
            logger.info(f"Speaking: {text}")
            
            # Use Windows SAPI for immediate speech
            self._speak_with_sapi(text)
            
            self.is_speaking = False
            
        except Exception as e:
            logger.error(f"Failed to speak text: {e}")
            self.is_speaking = False
    
    def _speak_with_sapi(self, text: str) -> bool:
        """Use Windows SAPI for TTS"""
        try:
            # Escape text for PowerShell
            escaped_text = text.replace('"', '""').replace("'", "''")
            
            # Create PowerShell command with better voice settings
            ps_command = f'''
            Add-Type -AssemblyName System.Speech
            $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
            $synth.Rate = 0
            $synth.Volume = 100
            $synth.Speak("{escaped_text}")
            '''
            
            # Execute PowerShell command
            result = subprocess.run([
                'powershell', '-Command', ps_command
            ], capture_output=True, text=True, timeout=15)
            
            return result.returncode == 0
            
        except Exception as e:
            logger.error(f"SAPI TTS error: {e}")
            return False
    
    def listen_for_command(self, timeout: int = 6, phrase_limit: int = 6) -> str:
        """Enhanced push-to-talk voice command listener"""
        
        # Prevent concurrent listening
        if not self._listening_lock.acquire(blocking=False):
            logger.warning("Voice recognition already in progress")
            return ""
        
        try:
            self._is_listening = True
            logger.info("Starting enhanced voice recognition...")
            
            # Multiple attempts for better accuracy
            for attempt in range(2):
                try:
                    with self.microphone as source:
                        # Fresh ambient noise adjustment for each attempt
                        logger.info(f"Attempt {attempt + 1}: Adjusting for ambient noise...")
                        self.recognizer.adjust_for_ambient_noise(source, duration=1.5)
                        
                        logger.info("Listening for voice command... Speak clearly now!")
                        
                        # Listen with enhanced settings
                        audio = self.recognizer.listen(
                            source, 
                            timeout=timeout, 
                            phrase_time_limit=phrase_limit
                        )
                    
                    # Recognition with multiple engines/methods
                    logger.info("Processing speech...")
                    
                    # Primary recognition method
                    try:
                        command = self.recognizer.recognize_google(
                            audio, 
                            language='en-US',
                            show_all=False
                        )
                        
                        if command and len(command.strip()) > 1:
                            logger.info(f"Successfully recognized: '{command}'")
                            return command.lower().strip()
                    
                    except sr.UnknownValueError:
                        logger.info(f"Attempt {attempt + 1}: Could not understand audio")
                        if attempt == 0:
                            continue  # Try again
                    
                    except sr.RequestError as e:
                        logger.error(f"Recognition service error: {e}")
                        return ""
                
                except sr.WaitTimeoutError:
                    logger.info(f"Attempt {attempt + 1}: Listening timeout")
                    if attempt == 0:
                        continue  # Try again
                    
                except Exception as e:
                    logger.error(f"Attempt {attempt + 1} failed: {e}")
            
            logger.info("All recognition attempts failed")
            return ""
            
        finally:
            self._is_listening = False
            self._listening_lock.release()
    
    def process_voice_command(self, command: str) -> str:
        """Process voice command using smart pattern matching"""
        if not command:
            return "unknown"
        
        # Use smart command processor
        action = self.command_processor.process_command(command)
        
        # Execute command-specific responses
        if action == "describe_scene":
            self.speak_immediately("Getting scene description", interrupt=True)
            
        elif action == "stop_talking":
            self.stop_speaking()
            self.speak_immediately("Okay, I'll be quiet")
            
        elif action == "repeat_last":
            self.speak_immediately("Repeating last message")
            
        elif action == "emergency":
            self.speak_immediately("Activating emergency mode", interrupt=True)
            
        elif action == "get_location":
            self.speak_immediately("Getting your location")
            
        elif action == "volume_up":
            self.speak_immediately("Volume increased")
            
        elif action == "volume_down":
            self.speak_immediately("Volume decreased")
            
        elif action == "speed_up":
            self.speak_immediately("Speech speed increased")
            
        elif action == "slow_down":
            self.speak_immediately("Speech speed decreased")
            
        elif action == "calibrate":
            self.speak_immediately("Starting calibration mode")
            
        elif action == "status":
            self.speak_immediately("VisionGuide AI is running normally")
            
        elif action == "unknown":
            # More helpful response for unrecognized commands
            self.speak_immediately("I didn't understand that. Try 'what do you see' or 'help me'")
        
        return action
    
    def _audio_worker(self):
        """Audio processing worker thread"""
        logger.info("Audio worker started")
        
        while self.running:
            try:
                # Get next message from queue
                try:
                    message = self.speech_queue.get(timeout=1.0)
                except queue.Empty:
                    continue
                
                # Skip if message is too old
                if time.time() - message.timestamp > 15:
                    continue
                
                # Skip empty messages
                if not message.text or message.text.strip() == "." or message.text.strip() == "":
                    continue
                
                # Speak the message
                self.is_speaking = True
                logger.info(f"Speaking: {message.text}")
                
                # Use Windows SAPI for speech
                self._speak_with_sapi(message.text)
                
                self.is_speaking = False
                
                # Call callback if provided
                if message.callback:
                    try:
                        message.callback()
                    except Exception as e:
                        logger.error(f"Callback error: {e}")
                
                # Mark task as done
                self.speech_queue.task_done()
                
                # Small delay
                time.sleep(0.2)
                
            except Exception as e:
                logger.error(f"Audio worker error: {e}")
                self.is_speaking = False
                time.sleep(0.5)
        
        logger.info("Audio worker stopped")
    
    def stop_speaking(self):
        """Stop current speech"""
        try:
            # Clear the speech queue
            while not self.speech_queue.empty():
                try:
                    self.speech_queue.get_nowait()
                except queue.Empty:
                    break
            
            self.is_speaking = False
            logger.info("Speech stopped and queue cleared")
            
        except Exception as e:
            logger.error(f"Failed to stop speech: {e}")
    
    def start(self):
        """Start audio processing"""
        if self.running:
            return
        
        self.running = True
        
        # Start audio worker thread
        self.audio_thread = threading.Thread(target=self._audio_worker)
        self.audio_thread.daemon = True
        self.audio_thread.start()
        
        logger.info("Audio processor started")
    
    def stop(self):
        """Stop audio processing"""
        self.running = False
        
        # Stop current speech
        self.stop_speaking()
        
        # Wait for thread to finish
        if self.audio_thread:
            self.audio_thread.join(timeout=5)
        
        logger.info("Audio processor stopped")
    
    def test_audio(self):
        """Test audio output with enhanced feedback"""
        self.speak_immediately("VisionGuide AI enhanced audio system is working correctly. Voice recognition ready.")
    
    def get_microphone_info(self):
        """Get information about available microphones"""
        try:
            mic_list = sr.Microphone.list_microphone_names()
            logger.info(f"Available microphones: {mic_list}")
            return mic_list
        except Exception as e:
            logger.error(f"Failed to get microphone info: {e}")
            return []
