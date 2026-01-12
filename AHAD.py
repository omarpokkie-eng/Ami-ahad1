#!/usr/bin/env python3
"""
Elite Hacker Terminal Generator with Password Security Feature
Creates a custom stylish terminal with your name!
"""

import os
import sys
import subprocess
from datetime import datetime

# ANSI Colors for Python output
class Colors:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    DARKGRAY = '\033[1;30m'
    GRAY = '\033[0;37m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_ascii_art(text):
    """Generate ASCII art from text using pyfiglet or fallback"""
    try:
        import pyfiglet
        return pyfiglet.figlet_format(text, font='standard')
    except ImportError:
        # Fallback: Simple ASCII art generator
        return generate_simple_ascii(text)

def generate_simple_ascii(text):
    """Fallback ASCII art generator"""
    # ... (Your original generate_simple_ascii function content) ...
    art = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║             {text.upper().center(43)}              ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    return art

def print_banner():
    """Print the welcome banner"""
    clear_screen()
    print(f"""
{Colors.CYAN}╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║             HACKERAHADCOLOUR - GENERATOR v3.1 (Secured)       ║
║                                                               ║
║             Create Your Custom Cyberpunk Terminal             ║
║                                                               ║
║           {Colors.GRAY}Credits: https://github.com/songworld061-png/Hackerahadcolour.git{Colors.CYAN}                             ║
║    {Colors.GRAY}GitHub: https://github.com/songworld061-png/Hackerahadcolour.git{Colors.CYAN}                      ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{Colors.RESET}
""")

def get_all_styles():
    """Return all 100 terminal styles"""
    # ... (Your original get_all_styles function content) ...
    return [
        # Original 20 styles
        ("1", "Standard", "Clean & Professional", "╰─➤", "GREEN"),
        ("2", "Advanced", "Maximum Effects", "┗━╼", "CYAN"),
        ("3", "Matrix", "Green Code Rain", "└──>", "GREEN"),
        ("4", "Neon Cyber", "Vibrant Neon Colors", "▶", "MAGENTA"),
        ("5", "Red Alert", "Red Hacker Theme", "⚠>", "RED"),
        ("6", "Ghost Protocol", "Stealth Mode", "»", "DARKGRAY"),
        ("7", "Dark Hacker", "Dark Minimalist", "→", "WHITE"),
        ("8", "Green Terminal", "Classic Green", "$", "GREEN"),
        ("9", "Blue Steel", "Cool Blue Theme", "►", "BLUE"),
        ("10", "Purple Haze", "Purple Aesthetic", "⟩", "MAGENTA"),
        
        # 10-20
        ("11", "Minimal", "Ultra Clean", ">", "WHITE"),
        ("12", "Retro DOS", "Old School DOS", "C:\\>", "YELLOW"),
        ("13", "Cyberpunk", "Cyberpunk 2077", "//»", "YELLOW"),
        ("14", "Anonymous", "Anonymous Style", "#>", "WHITE"),
        ("15", "Mr Robot", "fsociety Theme", "[!]>", "RED"),
        ("16", "Tron", "Tron Legacy", "◢◤>", "CYAN"),
        ("17", "Watchdogs", "ctOS Theme", "▰▰>", "BLUE"),
        ("18", "Black Hat", "Dark Ops", "●>", "RED"),
        ("19", "White Hat", "Security Pro", "○>", "GREEN"),
        ("20", "Elite", "Ultimate Hacker", "⟫", "CYAN"),
        
        # 21-40 - Movie/TV Inspired
        ("21", "Blade Runner", "Dystopian Future", "⟩⟩", "YELLOW"),
        ("22", "Ghost Shell", "Cybernetic", "◉>", "CYAN"),
        ("23", "Akira", "Neo Tokyo", "⚡>", "RED"),
        ("24", "Neuromancer", "Cyberspace", "▣>", "BLUE"),
        ("25", "Snow Crash", "Metaverse", "◈>", "WHITE"),
        ("26", "Black Mirror", "Dark Tech", "▼>", "DARKGRAY"),
        ("27", "Westworld", "AI Maze", "◇>", "YELLOW"),
        ("28", "Person Interest", "Machine", "⊡>", "BLUE"),
        ("29", "Halt Catch Fire", "Retro Tech", "⊚>", "GREEN"),
        ("30", "Silicon Valley", "Startup", "◐>", "CYAN"),
        
        # 31-50 - Game Inspired
        ("31", "Deus Ex", "Augmented", "⟐>", "YELLOW"),
        ("32", "System Shock", "SHODAN", "⟁>", "RED"),
        ("33", "Uplink", "Hacker Sim", "⊿>", "GREEN"),
        ("34", "Hacknet", "Terminal Game", "∴>", "CYAN"),
        ("35", "Shadowrun", "Cyberpunk RPG", "⬡>", "MAGENTA"),
        ("36", "Syndicate", "Corporate", "⬢>", "BLUE"),
        ("37", "Transistor", "Processing", "◬>", "RED"),
        ("38", "Observer", "Neural", "⊗>", "DARKGRAY"),
        ("39", "Ruiner", "Combat", "⊕>", "RED"),
        ("40", "Ghostrunner", "Cyber Ninja", "⟐", "CYAN"),
        
        # 41-60 - Tech Companies
        ("41", "Apple", "Think Different", "→", "WHITE"),
        ("42", "Google", "Colorful", "G>", "BLUE"),
        ("43", "Microsoft", "Azure", "⊞>", "BLUE"),
        ("44", "IBM", "Big Blue", "◈>", "BLUE"),
        ("45", "Oracle", "Database", "○>", "RED"),
        ("46", "Tesla", "Electric", "⚡>", "RED"),
        ("47", "SpaceX", "Rocket", "▲>", "WHITE"),
        ("48", "NASA", "Space", "★>", "BLUE"),
        ("49", "MIT", "Innovation", "∞>", "RED"),
        ("50", "CERN", "Particle", "◉>", "BLUE"),
        
        # 51-70 - Programming Languages
        ("51", "Python", "Simple Power", ">>>", "GREEN"),
        ("52", "JavaScript", "Web Power", "=>", "YELLOW"),
        ("53", "C++", "Performance", "::>", "BLUE"),
        ("54", "Rust", "Memory Safe", "|>", "RED"),
        ("55", "Go", "Concurrent", "go>", "CYAN"),
        ("56", "Ruby", "Elegant", "♦>", "RED"),
        ("57", "PHP", "Web Classic", "?>", "MAGENTA"),
        ("58", "Java", "Enterprise", "☕>", "RED"),
        ("59", "Swift", "iOS Native", "⚡>", "YELLOW"),
        ("60", "Kotlin", "Modern JVM", "K>", "MAGENTA"),
        
        # 61-80 - Hacker Terms
        ("62", "Root Access", "Full Control", "#>", "RED"),
        ("63", "Shell", "Command Line", "$>", "GREEN"),
        ("64", "Kernel", "Core System", "⊚>", "YELLOW"),
        ("65", "Daemon", "Background", "⊗>", "DARKGRAY"),
        ("66", "Firewall", "Protection", "⚠>", "RED"),
        ("67", "Exploit", "Vulnerability", "⚡>", "RED"),
        ("68", "Payload", "Code Inject", "◉>", "YELLOW"),
        ("69", "Backdoor", "Hidden Access", "◐>", "DARKGRAY"),
        ("70", "Crypter", "Encryption", "⊕>", "CYAN"),
        ("61", "Sudo", "Super User", "sudo>", "RED"),
        
        # 71-90 - OS/Distros
        ("71", "Kali Linux", "Pen Testing", "⟩>", "BLUE"),
        ("72", "Parrot OS", "Security", "🦜>", "CYAN"),
        ("73", "Ubuntu", "Humanity", "○>", "YELLOW"),
        ("74", "Arch", "I Use Arch", "▲>", "CYAN"),
        ("75", "Debian", "Stable", "◈>", "RED"),
        ("76", "Fedora", "Leading Edge", "∞>", "BLUE"),
        ("77", "CentOS", "Enterprise", "⊡>", "GREEN"),
        ("78", "Alpine", "Minimal", "⟩", "BLUE"),
        ("79", "Gentoo", "Compile", "∴>", "MAGENTA"),
        ("80", "BSD", "Berkeley", "◉>", "RED"),
        
        # 91-100 - Cyber Terms
        ("81", "Zero Day", "Unknown Vuln", "0>", "RED"),
        ("82", "DDoS", "Flood Attack", "▰▰▰>", "RED"),
        ("83", "Phishing", "Social Eng", "⚓>", "YELLOW"),
        ("84", "Ransomware", "Crypto Lock", "🔒>", "RED"),
        ("85", "Botnet", "Zombie Army", "⊚⊚>", "DARKGRAY"),
        ("86", "Malware", "Evil Code", "⚠⚠>", "RED"),
        ("87", "Trojan", "Hidden Threat", "🐴>", "YELLOW"),
        ("88", "Rootkit", "Deep Hide", "⊗>", "DARKGRAY"),
        ("89", "Keylogger", "Key Capture", "⌨>", "CYAN"),
        ("90", "RAT", "Remote Control", "🐀>", "RED"),
        ("91", "SQL Inject", "DB Attack", "';>", "BLUE"),
        ("92", "XSS", "Script Inject", "<>", "YELLOW"),
        ("93", "CSRF", "Cross-Site", "⟳>", "RED"),
        ("94", "Brute Force", "Try All", "###>", "RED"),
        ("95", "Dictionary", "Word List", "📖>", "GREEN"),
        ("96", "Rainbow Table", "Hash Crack", "🌈>", "MAGENTA"),
        ("97", "Man Middle", "Intercept", "↔>", "YELLOW"),
        ("98", "Sniffing", "Packet Capture", "👃>", "CYAN"),
        ("99", "Spoofing", "Fake Identity", "🎭>", "WHITE"),
        ("100", "Steganography", "Hidden Data", "🖼>", "BLUE"),
        ("101", "Remove", "Uninstall Terminal", "", "RED"),
    ]

def get_user_input():
    """Get user's name and preferences"""
    # First, ask for option
    print(f"{Colors.CYAN}╔═══════════════════════════════════════════════════════════════╗")
    print(f"║           SELECT YOUR HACKER TERMINAL STYLE (1-101)           ║")
    print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    styles = get_all_styles()
    
    # Display in 2 columns
    mid = len(styles) // 2
    for i in range(mid):
        left = styles[i]
        right = styles[i + mid] if i + mid < len(styles) else None
        
        left_num, left_name, left_desc, left_symbol, left_color = left
        left_color_obj = getattr(Colors, left_color, Colors.WHITE)
        
        if left_num == "101":
            print(f"\n{Colors.RED}  [{left_num}] {left_name:<15} - {left_desc}{Colors.RESET}")
        else:
            left_str = f"{Colors.GREEN}[{left_num.rjust(3)}]{Colors.RESET} {Colors.WHITE}{left_name:<15}{Colors.RESET} {left_color_obj}{left_symbol:<8}{Colors.RESET}"
            
            if right:
                right_num, right_name, right_desc, right_symbol, right_color = right
                right_color_obj = getattr(Colors, right_color, Colors.WHITE)
                right_str = f"{Colors.GREEN}[{right_num.rjust(3)}]{Colors.RESET} {Colors.WHITE}{right_name:<15}{Colors.RESET} {right_color_obj}{right_symbol:<8}{Colors.RESET}"
                print(f"  {left_str}  {right_str}")
            else:
                print(f"  {left_str}")
    
    while True:
        style = input(f"\n{Colors.CYAN}▸ Select style [1-101]: {Colors.RESET}").strip()
        if style in [str(i) for i in range(1, 102)]:
            break
        print(f"{Colors.RED}✗ Please enter a number between 1-101{Colors.RESET}")
    
    # If removing, skip name and color
    if style == '101':
        return None, style, None, None
    
    # Ask for name
    print(f"\n{Colors.YELLOW}Enter your details:{Colors.RESET}\n")
    while True:
        name = input(f"{Colors.GREEN}▸ Enter your name/handle: {Colors.RESET}").strip()
        if name:
            break
        print(f"{Colors.RED}✗ Name cannot be empty!{Colors.RESET}")

    # Ask for password setting
    print(f"\n{Colors.CYAN}Set a login password (Optional, recommended):{Colors.RESET}\n")
    while True:
        password = input(f"{Colors.GREEN}▸ Set Password (Leave blank for '1234'): {Colors.RESET}").strip()
        if not password:
            password = '1234' # Default password
        
        import hashlib
        # Hash the password (we use MD5 for simplicity in bash scripts)
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        print(f"{Colors.YELLOW}ⓘ Password Hash (MD5): {password_hash}{Colors.RESET}")
        break
    
    # Ask for color customization
    print(f"\n{Colors.CYAN}Choose your color scheme:{Colors.RESET}\n")
    print(f"  {Colors.GREEN}[1]{Colors.RESET} {Colors.GREEN}Green{Colors.RESET}    - Classic Hacker")
    print(f"  {Colors.RED}[2]{Colors.RESET} {Colors.RED}Red{Colors.RESET}      - Alert/Danger")
    print(f"  {Colors.BLUE}[3]{Colors.RESET} {Colors.BLUE}Blue{Colors.RESET}     - Cool/Tech")
    print(f"  {Colors.CYAN}[4]{Colors.RESET} {Colors.CYAN}Cyan{Colors.RESET}     - Matrix Style")
    print(f"  {Colors.MAGENTA}[5]{Colors.RESET} {Colors.MAGENTA}Magenta{Colors.RESET}  - Neon/Purple")
    print(f"  {Colors.YELLOW}[6]{Colors.RESET} {Colors.YELLOW}Yellow{Colors.RESET}   - Bright/Warning")
    print(f"  {Colors.WHITE}[7]{Colors.RESET} {Colors.WHITE}White{Colors.RESET}    - Clean/Minimal")
    print(f"  {Colors.GRAY}[8]{Colors.RESET} {Colors.DARKGRAY}Gray{Colors.RESET}     - Dark/Stealth")
    print(f"  {Colors.WHITE}[9]{Colors.RESET} Default  - Use style's color")
    
    while True:
        color_choice = input(f"\n{Colors.GREEN}▸ Select color [1-9]: {Colors.RESET}").strip()
        if color_choice in [str(i) for i in range(1, 10)]:
            break
        print(f"{Colors.RED}✗ Please enter a number between 1-9{Colors.RESET}")
    
    color_map = {
        '1': 'GREEN', '2': 'RED', '3': 'BLUE', '4': 'CYAN',
        '5': 'MAGENTA', '6': 'YELLOW', '7': 'WHITE', '8': 'DARKGRAY', '9': None
    }
    
    custom_color = color_map.get(color_choice)
    
    return name, style, custom_color, password_hash

# --- Other functions (create_welcome_script, create_advanced_script, create_launcher, remove_terminal) are removed for brevity, as they were not modified except for calling the new function ---
# The logic from these functions can be consolidated into the main creation function.

def setup_auto_startup(script_name):
    """Setup auto-startup by adding to .bashrc with auto-fix"""
    bashrc_path = os.path.expanduser("~/.bashrc")
    script_path = os.path.join(os.getcwd(), script_name)
    
    try:
        # Backup .bashrc first
        if os.path.exists(bashrc_path):
            import shutil
            shutil.copy(bashrc_path, bashrc_path + '.backup_auto')
        
        # Read current .bashrc
        existing_content = ""
        if os.path.exists(bashrc_path):
            with open(bashrc_path, 'r') as f:
                existing_content = f.read()
        
        # Auto-fix: Remove old entries (with or without 'source')
        if 'welcome.sh' in existing_content or 'welcome_advanced.sh' in existing_content or 'elite_terminal_' in existing_content or 'Terminal Auto-Start' in existing_content:
            print(f"{Colors.YELLOW}  ⚠ Detected old installation - Auto-fixing...{Colors.RESET}")
            
            lines = existing_content.split('\n')
            new_lines = []
            skip_next = False
            
            for line in lines:
                # Skip comment line
                if 'Terminal Auto-Start' in line or 'WELCOME Terminal Auto-Start' in line or 'ELITE_TERMINAL' in line:
                    skip_next = True
                    continue
                # Skip the actual script line
                if skip_next and ('welcome.sh' in line or 'welcome_advanced.sh' in line or 'elite_terminal_' in line):
                    skip_next = False
                    continue
                new_lines.append(line)
            
            # Write cleaned content
            with open(bashrc_path, 'w') as f:
                f.write('\n'.join(new_lines))
            
            print(f"{Colors.GREEN}  ✓ Cleaned old entries{Colors.RESET}")
        
        # Add new entry with source command (important for PS1 to persist!)
        with open(bashrc_path, 'a') as f:
            f.write(f"\n# ELITE_TERMINAL Auto-Start\n")
            f.write(f"source {script_path}\n")
        
        print(f"{Colors.GREEN}  ✓ Added to startup (.bashrc) with 'source'{Colors.RESET}")
        return True
    except Exception as e:
        print(f"{Colors.RED}  ✗ Could not add to startup: {e}{Colors.RESET}")
        return False

def remove_terminal():
    """Remove terminal files and startup entries - restore normal Termux prompt"""
    print(f"\n{Colors.YELLOW}Removing Stylish Terminal...{Colors.RESET}\n")
    
    # We remove all generated scripts, not just the original two
    files_to_remove = [f for f in os.listdir('.') if f.startswith('elite_terminal_') and f.endswith('.sh')]
    files_to_remove.extend(['welcome.sh', 'welcome_advanced.sh', 'launcher.sh', 'README.md'])
    
    removed_count = 0
    
    for file in set(files_to_remove): # Use set to avoid duplicates
        if os.path.exists(file):
            try:# Ami-ahad1
