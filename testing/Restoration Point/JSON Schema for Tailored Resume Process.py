{
  "personal_information": {
    "name": "string",
    "contact_info": {
      "phone": "string",
      "email": "string",
      "location": "string",
      "linkedin": "string"
    }
  },
  "summary": {
    "content": "string",
    "rules": [
      "Must summarize experience relevant to the job description",
      "Keep within 2-3 lines"
    ]
  },
  "skills": {
    "static": ["Technical Skills", "Leadership Skills"],
    "dynamic": ["Skills derived from job description"],
    "rules": [
      "Must align with skills mentioned in the job description",
      "Avoid duplicates and unrelated skills"
    ]
  },
  "experience": {
    "roles": [
      {
        "company": "string",
        "title": "string",
        "location": "string",
        "dates": "string",
        "responsibilities": [
          "string"
        ],
        "rules": [
          "Prioritize responsibilities that align with job description",
          "Limit bullets to 5 per role"
        ]
      }
    ]
  },
  "education": {
    "entries": [
      {
        "school": "string",
        "degree": "string",
        "location": "string",
        "focus": "string"
      }
    ]
  },
  "key_achievements": {
    "entries": [
      {
        "title": "string",
        "description": "string",
        "rules": [
          "Highlight measurable outcomes",
          "Avoid vague or generic achievements"
        ]
      }
    ]
  },
  "projects": {
    "entries": [
      {
        "title": "string",
        "goal": "string",
        "responsibilities": "string",
        "results": "string"
      }
    ],
    "rules": [
      "Prioritize projects relevant to the job description",
      "Include measurable results wherever possible"
    ]
  },
  "tailoring_rules": {
    "global_rules": [
      "Avoid duplicate verbs across all sections",
      "Ensure ATS compatibility by using simple formatting",
      "Prioritize relevant details per the job description"
    ],
    "sectional_rules": [
      "Summary must align with key job responsibilities",
      "Skills section must directly reflect job requirements"
    ],
    "cross_sectional_rules": [
      "Consistent verb usage between Experience and Projects",
      "No repeated phrases in Summary and Key Achievements"
    ]
  }
}
