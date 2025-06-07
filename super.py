import streamlit as st

st.title("📘 MT Business School - Accounting Quiz")

questions = [
    {
        "question": "1. What does the accounting equation state?",
        "options": ["Assets = Liabilities + Equity", "Assets = Income - Expenses", "Assets = Liabilities - Equity", "Assets = Cash + Capital"],
        "answer": "Assets = Liabilities + Equity"
    },
    {
        "question": "2. Which financial statement shows a company’s revenues and expenses?",
        "options": ["Balance Sheet", "Cash Flow Statement", "Income Statement", "Statement of Equity"],
        "answer": "Income Statement"
    },
    {
        "question": "3. What is depreciation?",
        "options": ["A reduction in inventory", "Allocation of an asset’s cost over its useful life", "A tax expense", "Revenue adjustment"],
        "answer": "Allocation of an asset’s cost over its useful life"
    },
    {
        "question": "4. Which account is increased with a debit?",
        "options": ["Revenue", "Liabilities", "Expenses", "Equity"],
        "answer": "Expenses"
    },
    {
        "question": "5. What is the normal balance of a liability account?",
        "options": ["Debit", "Credit", "Zero", "Fluctuates"],
        "answer": "Credit"
    },
    {
        "question": "6. Which principle requires accountants to report all relevant information?",
        "options": ["Conservatism Principle", "Full Disclosure Principle", "Revenue Recognition Principle", "Matching Principle"],
        "answer": "Full Disclosure Principle"
    },
    {
        "question": "7. What is an accrued expense?",
        "options": ["Expense paid in advance", "Revenue not yet received", "Expense incurred but not yet paid", "None of the above"],
        "answer": "Expense incurred but not yet paid"
    },
    {
        "question": "8. Which of the following is a current asset?",
        "options": ["Equipment", "Accounts Payable", "Accounts Receivable", "Loan Payable"],
        "answer": "Accounts Receivable"
    },
    {
        "question": "9. What type of account is 'Unearned Revenue'?",
        "options": ["Asset", "Liability", "Equity", "Expense"],
        "answer": "Liability"
    },
    {
        "question": "10. The matching principle matches:",
        "options": ["Assets with Liabilities", "Revenue with Expenses", "Cash with Capital", "Income with Drawings"],
        "answer": "Revenue with Expenses"
    }
]

score = 0
for i, q in enumerate(questions):
    st.subheader(q["question"])
    selected = st.radio("", q["options"], key=i)
    if selected == q["answer"]:
        score += 1

if st.button("Submit Quiz"):
    st.success(f"🎉 You scored {score} out of {len(questions)}")

