import time
import random
# Define the fake documents for each agency
FAKE_DOCUMENTS = {
    'FBI': [
        "Operation Night Sky - 2023-04-01",
        "Project Eagle Eye - 2023-05-15",
        "Operation Silent Shadow - 2023-06-10",
        "Crimson Codebreaker - 2023-07-20",
        "Project Black Falcon - 2023-08-05",
        "Operation Midnight Mirage - 2023-09-15",
        "Project Shadow Strike - 2023-10-20",
        "Operation Thunderstorm - 2023-11-05",
        "Project Steel Serpent - 2023-12-10",
        "Operation Ice Phoenix - 2024-01-15"
    ],

    'CIA': [
        "Project Insight - 2023-04-05",
        "Operation Dark Phoenix - 2023-05-20",
        "Black Widow Protocol - 2023-06-15",
        "Quantum Surveillance Matrix - 2023-07-25",
        "Ghost Protocol - 2023-08-10",
        "Operation Red Tiger - 2023-09-25",
        "Project Blue Falcon - 2023-10-30",
        "Operation Golden Eagle - 2023-11-15",
        "Black Diamond Initiative - 2023-12-20",
        "Operation Jade Serpent - 2024-01-25"
    ],

    'NSA': [
        "Surveillance Protocol X - 2023-04-10",
        "Quantum Data Interceptor - 2023-05-25",
        "Operation Cyber Shield - 2023-06-20",
        "Echelon 2.0 - 2023-07-30",
        "Project Quantum Leap - 2023-08-15",
        "Operation Solar Flare - 2023-09-30",
        "Quantum Encryption Project - 2023-10-15",
        "Operation Silent Watch - 2023-11-30",
        "Project Icebreaker - 2023-12-15",
        "Operation Shadow Blade - 2024-01-30"
    ],

    'DHS': [
        "Operation Eagle Eye - 2023-04-10",
        "Project Homeland Security - 2023-05-25",
        "Operation Border Watch - 2023-06-20",
        "Cyber Defense Initiative - 2023-07-30",
        "Project Safe Harbor - 2023-08-15",
        "Operation Cyber Guardian - 2023-09-30",
        "Border Patrol Enhancement - 2023-10-15",
        "Operation Sky Sentinel - 2023-11-30",
        "Critical Infrastructure Protection - 2023-12-15",
        "Operation Firestorm - 2024-01-30"
    ],

    'MI6': [
        "Operation Silent Fox - 2023-04-15",
        "Project Thunderbolt - 2023-05-30",
        "Operation Shadow Hunter - 2023-06-25",
        "Quantum Espionage Initiative - 2023-08-05",
        "Operation Black Swan - 2023-09-10",
        "Project Skyfall - 2023-10-25",
        "Operation Ice Dragon - 2023-11-10",
        "Covert Surveillance Protocol - 2023-12-25",
        "Project Stealth Panther - 2024-01-10",
        "Operation Midnight Serenade - 2024-02-15"
    ],

    'GCHQ': [
        "Operation Quantum Shield - 2023-04-20",
        "Project Cybernetic Owl - 2023-06-05",
        "Operation Silent Breeze - 2023-07-10",
        "Quantum Intelligence Matrix - 2023-08-25",
        "Operation Dark Falcon - 2023-09-10",
        "Project Skywatch - 2023-10-25",
        "Operation Lunar Eclipse - 2023-11-10",
        "Advanced Cyber Threat Analysis - 2023-12-25",
        "Operation Nightshade - 2024-01-10",
        "Quantum Surveillance Network - 2024-02-25"
    ],

    'MSS': [
        "Operation Dragon's Breath - 2023-05-01",
        "Project Red Phoenix - 2023-06-15",
        "Operation Silent Tiger - 2023-07-10",
        "Golden Shield Initiative - 2023-08-25",
        "Project Silk Road - 2023-09-10",
        "Operation Jade Dragon - 2023-10-25",
        "Quantum Espionage Protocol - 2023-11-10",
        "Operation Black Panda - 2023-12-25",
        "Project Shadow Lotus - 2024-01-10",
        "Operation Iron Wall - 2024-02-25"
    ],

    'FSB': [
        "Operation Red Bear - 2023-05-05",
        "Project Siberian Storm - 2023-06-20",
        "Operation Arctic Fox - 2023-07-15",
        "Kremlin Cyber Defense Initiative - 2023-08-30",
        "Project Volga Vortex - 2023-09-15",
        "Operation Ural Eagle - 2023-10-30",
        "Quantum Surveillance Kremlin - 2023-11-15",
        "Operation Moscow Shield - 2023-12-30",
        "Project Russian Roulette - 2024-01-15",
        "Operation Siberian Star - 2024-02-28"
    ],

    'RAW': [
        "Operation Tiger's Roar - 2023-05-10",
        "Project Black Cobra - 2023-06-25",
        "Operation Eagle Eye - 2023-07-20",
        "Cybernetic Surveillance Initiative - 2023-09-04",
        "Project Silent Hawk - 2023-10-20",
        "Operation Phantom Mirage - 2023-11-05",
        "Quantum Reconnaissance Protocol - 2023-12-20",
        "Project Steel Griffin - 2024-01-05",
        "Operation Desert Fox - 2024-02-20",
        "Project Crimson Dragon - 2024-03-06"
    ]
}


def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_case_file(agency_name, documents):
    print_slow(f"\n\033[91m███╗   ███╗ █████╗ ███████╗███████╗    ███████╗███████╗ ██████╗ ██████╗ \033[0m")
    print_slow(f"\033[91m████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔════╝██╔════╝██╔═══██╗██╔══██╗\033[0m")
    print_slow(f"\033[91m██╔████╔██║███████║███████╗███████╗    ███████╗███████╗██║   ██║██████╔╝\033[0m")
    print_slow(f"\033[91m██║╚██╔╝██║██╔══██║╚════██║╚════██║    ╚════██║╚════██║██║   ██║██╔══██╗\033[0m")
    print_slow(f"\033[91m██║ ╚═╝ ██║██║  ██║███████║███████║    ███████║███████║╚██████╔╝██║  ██║\033[0m")
    print_slow(f"\033[91m╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝\033[0m")
    print_slow(f"\033[91m                             Government Hacking Simulator (GHS)\033[0m\n")

    for document in documents:
        print_slow(f"\033[91m{document}\033[0m", delay=0.02)

    print_slow(f"\n\033[91mDocument extraction complete for {agency_name}.\n\033[0m")
    time.sleep(1)

def hack_agency(agency_name):
    print_slow(f"\n\033[91mInitiating connection to {agency_name}...\033[0m")
    time.sleep(1)
    print_slow(f"\033[91mAccessing secure servers of {agency_name}...\033[0m")
    
    for i in range(11):
        progress = i * 10
        time.sleep(random.uniform(0.2, 0.5))
        print_slow(f"\033[92mHacking {agency_name} databases... {progress}%\033[0m", delay=0.02)

    time.sleep(1)
    print_slow(f"\n\033[96mAccess granted. Retrieving confidential documents from {agency_name}...\n\033[0m")
    time.sleep(2)
    display_case_file(agency_name, FAKE_DOCUMENTS[agency_name])

def main():
    agencies = ['FBI', 'CIA', 'NSA', 'DHS', 'MI6', 'GCHQ', 'MSS', 'FSB', 'RAW']

    print_slow(f"\033[95m{'*' * 50}\033[0m")
    print_slow(f"\033[95m{'Welcome to the Government Hacking Simulator!':^50}\033[0m")
    print_slow(f"\033[95m{'*' * 50}\033[0m\n")

    while agencies:
        agency = random.choice(agencies)
        agencies.remove(agency)
        hack_agency(agency)

    print_slow("\033[91mStay put, authorities are on their way!\033[0m")
    time.sleep(30)
    print_slow("\033[95mThis is just a simulation and is not real.\033[0m")

if __name__ == '__main__':
    main()
