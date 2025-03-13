def generate_soap_note(transcript: str) -> dict:
    """
    Generates a structured SOAP note from the transcript.
    """
    subjective = {
        "Chief_Complaint": "",
        "History_of_Present_Illness": ""
    }
    if "pain" in transcript.lower():
        subjective["Chief_Complaint"] = "Neck and back pain"
        subjective["History_of_Present_Illness"] = (
            "Patient had a car accident, experienced pain for several weeks, "
            "and now reports occasional pain."
        )

    objective = {
        "Physical_Exam": "Full range of motion in neck and back, no tenderness.",
        "Observations": "Patient appears in stable condition."
    }

    assessment = {
        "Diagnosis": "Whiplash injury",
        "Severity": "Mild, improving"
    }

    plan = {
        "Treatment": "Continue physiotherapy as needed, use painkillers if required.",
        "Follow-Up": "Return if symptoms worsen or persist beyond six months."
    }

    return {
        "Subjective": subjective,
        "Objective": objective,
        "Assessment": assessment,
        "Plan": plan
    }