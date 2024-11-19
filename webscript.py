#Todo finish this function
import urllib.request
def get_readme_data() -> str: #place holder for the url
    fp = urllib.request.urlopen("https://raw.githubusercontent.com/dmccrthy/CyberPatriot-Tools/refs/heads/main/Sample%20Content/Sample_README.html") #README url here
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

#Todo finish this function
def parse_readme_data(data: str) -> list[str]:
    # Initialize lists to store different sections
    competition_scenario = []
    authorized_admins = []
    authorized_users = []
    critical_services = []
    
    # Split data into lines
    lines = data.split('\n')
    
    # Track current section
    current_section = None
    
    # Parse through lines
    for line in lines:
        line = line.strip()
        
        # Identify sections
        if "Competition Scenario" in line:
            current_section = "scenario"
            continue
        elif "Authorized Administrators:" in line:
            current_section = "admins" 
            continue
        elif "Authorized Users:" in line:
            current_section = "users"
            continue
        elif "Critical Services:" in line:
            current_section = "services"
            continue
            
        # Skip empty lines
        if not line:
            continue
            
        # Add content to appropriate section
        if current_section == "scenario":
            if line.startswith("<h2>"):
                current_section = None
            elif not line.startswith(("<p>", "</p>", "<b>", "</b>")):
                competition_scenario.append(line)
                
        elif current_section == "admins":
            if not line.startswith(("<pre>", "</pre>", "<b>")):
                if "\t" not in line and line != "Authorized Users:":
                    authorized_admins.append(line)
                    
        elif current_section == "users":
            if not line.startswith(("</pre>", "<b>", "</b>")):
                authorized_users.append(line)
                
        elif current_section == "services":
            if line.startswith("<li>"):
                service = line.replace("<li>", "").replace("</li>", "").strip()
                if service != "(None)":
                    critical_services.append(service)
    
    # Clean up users list
    authorized_users = [user for user in authorized_users if user]
    
    return [
        competition_scenario,
        {
            "administrators": authorized_admins,
            "users": authorized_users
        },
        critical_services
    ]

def writeFiles(data: list[str]) -> None:
    with open("scenario.txt", "w") as file:
        file.write(data[0])
            
    with open("services.txt", "w") as file:
        for service in data[2]:
            file.write(service + "\n")
            
    from customfunctions import run_command
    current_users = run_command("cut -d: -f1 /etc/passwd")    
    
    with open("admins.txt", "w") as file:
        for admin in data[1]["administrators"]:
            if admin in current_users:
                file.write(admin + "\n")
            
    with open("normal_users.txt", "w") as file:
        for user in data[1]["users"]:
            if user in current_users:
                file.write(user + "\n")
                
    with open("new_users.txt", "w") as file:
        for user in data[1]["users"]:
            if user not in current_users:
                file.write(user + "\n")

    with open("remove_users.txt", "w") as file:
        for user in current_users:
            if user not in data[1]["users"]:
                file.write(user + "\n")
