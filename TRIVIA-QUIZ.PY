Question = {
"who is firs prime minister of india?": "jawallal nehru",
"How many time to build the constitution?": "3year, 11month, 18days"
}
def ask_solution(Question, answer):
    user = input(f"{Question}").strip() .lower()
    return user == answer

score = 0

for q, a in Question.items():
    if  ask_solution(q, a):
        print("correct! ✔️")
    else:
        print(f"Nnoop! answer is wrong ❌ {a}.")

print(f"\n your final score: {score}/{len(Question)}")