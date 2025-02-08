import json

def tailor_resume(json_path):
    with open(json_path, "r") as file:
        data = json.load(file)
    
    print("Tailored Resume")
    print("="*20)
    print(f"Name: {data['personal_information']['name']}")
    print(f"Contact: {data['personal_information']['contact_info']}")
    print("\nSummary:")
    print(data['summary']['content'])
    print("\nSkills:")
    print(", ".join(data['skills']['static']))
    print("\nExperience:")
    for role in data['experience']['roles']:
        print(f"{role['company']} | {role['title']} | {role['location']} | {role['dates']}")
        for responsibility in role['responsibilities']:
            print(f"- {responsibility}")
    print("\nEducation:")
    for edu in data['education']['entries']:
        print(f"{edu['school']} | {edu['degree']} | {edu['location']}")
    print("\nKey Achievements:")
    for achievement in data['key_achievements']['entries']:
        print(f"{achievement['title']}: {achievement['description']}")
    print("\nProjects:")
    for project in data['projects']['entries']:
        print(f"{project['title']} | {project['goal']} | {project['results']}")

if __name__ == "__main__":
    tailor_resume("scripts/json_schema.json")
