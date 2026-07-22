def print_report(
    overall_score,
    semantic_score,
    required_skill_score,
    ats_score,
    skills,
    matched_skills,
    missing_skills,
    feedback,
    candidate,
):
    print("=" * 50)
    print("AI Recruitment Assistant Report")
    print("=" * 50)
    print("\nCandidate Information")
    print("-" * 30)
    print(f"Name  : {candidate['name']}")
    print(f"Email : {candidate['email']}")
    print(f"Phone : {candidate['phone']}")

    print(f"\nOverall Match       : {overall_score}%")
    print(f"Semantic Match      : {semantic_score}%")
    print(f"Required Skills     : {required_skill_score}%")
    print(f"ATS Score           : {ats_score}/100")

    print("\nDetected Skills")
    print("-" * 30)
    
    for skill in skills:
        print(f"✓ {skill}")

    print("\nMatched Skills")
    print("-" * 30)

    for skill in matched_skills:
        print(f"✓ {skill}")

    print("\nMissing Skills")
    print("-" * 30)

    for skill in missing_skills:
        print(f"✗ {skill}")
    
    if feedback:
        print("\nATS Suggestions")
        print("-" * 30)

        for item in feedback:
            print(f"• {item}")
    print("\n" + "=" * 50)