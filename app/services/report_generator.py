def print_report(match_score, ats_report, resume):
    print("=" * 50)
    print("AI Recruitment Assistant Report")
    print("=" * 50)
    print("\nCandidate Information")
    print("-" * 30)
    print(f"Name  : {resume.name}")
    print(f"Email : {resume.email}")
    print(f"Phone : {resume.phone}")

    print(f"\nResume Match Score : {match_score:.2f}%")
    print(f"ATS Score          : {ats_report['score']}/100")

    print("\nDetected Skills")
    print("-" * 30)

    for skill in resume.skills:
        print(f"✓ {skill}")

    if ats_report["feedback"]:
        print("\nATS Suggestions")
        print("-" * 30)

        for item in ats_report["feedback"]:
            print(f"• {item}")
    print("\n" + "=" * 50)