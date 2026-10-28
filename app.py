            st.session_state.quiz_answers.get(str(i)) == QUIZ_QUESTIONS[i]["answer"]
            for i in order
        )
        st.metric("Your score", f"{correct} / {len(order)}", f"{round(correct / len(order) * 100)}%")
        for position, i in enumerate(order, start=1):
            q = QUIZ_QUESTIONS[i]
            answer = st.session_state.quiz_answers.get(str(i), "No answer")
            with st.expander(f"{'✅' if answer == q['answer'] else '❌'} Q{position}: {q['topic']}"):
                st.write(q["question"])
                st.write(f"**Your answer:** {answer}")
                st.write(f"**Correct answer:** {q['answer']}")
                st.write(q["explanation"])
        if st.button("Try quiz again", type="primary"):
            reset_quiz()
            st.rerun()
    else:
        for position, i in enumerate(st.session_state.quiz_order, start=1):
            q = QUIZ_QUESTIONS[i]
            st.markdown(f"**Q{position}. {q['question']}**")
            st.session_state.quiz_answers[str(i)] = st.radio(
                "Choose one answer",
                q["options"],
                key=f"quiz_q_{i}",
                index=None,
                label_visibility="collapsed",
            )
            st.caption(f"Topic: {q['topic']}")
            st.divider()
        if st.button("Submit quiz", type="primary", use_container_width=True):
            st.session_state.quiz_submitted = True
            correct = sum(
                st.session_state.quiz_answers.get(str(i)) == QUIZ_QUESTIONS[i]["answer"]
                for i in st.session_state.quiz_order
            )
            if award_xp("quiz_completed", 30):
                st.session_state.xp += max(0, correct * 2)
            st.rerun()

# ----------------------------- Safety Scenarios ----------------------------
elif page == "Safety Scenarios":
    mark_module_visited(page)
    st.subheader("🧭 What Would You Do?")
    st.write("Practice choosing a safer response to everyday online situations.")
    situations = [
        {
            "title": "A caller asks for your OTP",
            "prompt": "Someone claiming to be from your bank says they need your one-time code to stop fraud.",
            "options": [
                "Give the code because they sound professional",
                "Hang up and contact the bank using its official number or app",
                "Send the code by text instead",
            ],
            "answer": "Hang up and contact the bank using its official number or app",
            "explanation": "Never share one-time codes. Contact the bank through a trusted channel you find independently.",
        },
        {
            "title": "A friend sends a strange link",
            "prompt": "A friend's account sends an unexpected message asking you to sign in urgently.",
            "options": [
                "Sign in immediately",
                "Ask the friend through another channel if they sent it",
                "Forward the link to your group chat",
            ],
            "answer": "Ask the friend through another channel if they sent it",
            "explanation": "Accounts can be compromised. Verify unexpected requests through a different trusted channel and avoid the link.",
        },
        {
            "title": "A public computer remembers you",
            "prompt": "You used a shared computer to check your email and notice your account is still signed in.",
            "options": [
                "Leave it for the next person",
                "Sign out, close the session, and avoid saving credentials on shared devices",
                "Save the password for convenience",
            ],
            "answer": "Sign out, close the session, and avoid saving credentials on shared devices",
            "explanation": "Always sign out from shared devices. If you suspect someone accessed your account, secure it from your own device.",
        },
    ]
    for i, situation in enumerate(situations):
        with st.expander(situation["title"], expanded=(i == 0)):
            st.write(situation["prompt"])
            response = st.radio("Choose the safest action", situation["options"], key=f"situation_{i}")
            if st.button("Check decision", key=f"situation_check_{i}"):
                if response == situation["answer"]:
                    st.success("Good choice!")
                    if award_xp(f"situation_{i}", 10):
                        st.toast("You earned 10 XP!")
                else:
                    st.warning("Try again. Think about how to verify the request independently.")
                st.write(situation["explanation"])

# ----------------------------------- About ---------------------------------
elif page == "About":
    st.subheader("About CyberSmart Academy")
    st.write(
        "CyberSmart Academy is a beginner-friendly educational demo that teaches practical digital safety through simulated messages, quizzes, and decision-making scenarios."
    )
    st.markdown("#### Learning topics")
    st.markdown(
        "- Recognising phishing and social engineering\n"
        "- Creating and protecting strong, unique passwords\n"
        "- Keeping one-time codes private\n"
        "- Safer browsing, updates, backups, and privacy\n"
        "- Responding when an account may be compromised"
    )
    st.warning(
        "Educational disclaimer: This app provides general awareness training. Its password score is a simplified estimate, not a security audit. Training messages are fictional and must not be treated as evidence about a real sender."
    )
    st.markdown("#### Built with")
    st.write("Python · Streamlit · Session State")
    st.markdown("[Streamlit Community Cloud](https://share.streamlit.io/)")

st.divider()
st.caption("CyberSmart Academy • Learn responsibly. Stay curious. Stay safe.")
