# Email Security Agents 🚀

This project demonstrates an **Email Security Agent system** built using the Google ADK framework.

---

## 🖼️ Conversation Snapshot
Here’s an example chat session with the agents:

![Conversation Screenshot](conversation_snapshot.png)

---
### Event Flow – Page 1

![Event Flow Page 1](./event_flow_page1.png)

This event flow shows how the **Email Security Agent system** is structured:

- **SequentialAgent Framework** is used for:
  - **GreetingAgent** → Handles user greetings and routes input.
  - **ClassifierAgent** → Coordinates the parallel checks.
  - **ExplainerAgent** → Summarizes the classification process and results.
  - **AdvisorAgent** → Provides final security recommendations to the user.

- **ParallelAgent Framework** is used for:
  - **PhishingEmailDetectorAgent** → Detects phishing emails.
  - **AttachmentCheckerAgent** → Analyzes file attachments.
  - **LinkCheckerAgent** → Inspects links/URLs.

- **Function Tool: `classify_email`**
  - Tools are created by you and tailored to your application.
  - Functions/Methods are defined as standard synchronous functions (e.g., Python `def`) in the code.
  - Here, `classify_email` is the function tool used to trigger email classification.

- **Model Files Used**
  - For the **PhishingEmailDetectorAgent**, I integrated models from my earlier project:  
    - `logistic_regression.joblib`  
    - `tfidf_vectorizer.joblib`  
  - These were imported directly from my GitHub repository:  
    [Phishing-Email-Detecting](https://github.com/Venksaiabhishek/Phishing-Email-Detecting)

This design ensures that:
- Initial interaction and summary steps follow a **sequential pipeline**.  
- Heavy security analysis tasks (phishing, attachments, links) run **in parallel** for efficiency.  

## 📑 Event Flow Diagram
The detailed session event flow is available as a PDF:  
👉 [Download Event Flow Diagram](event_flow_diagram.pdf)
## 📊 Event Session Flow

Or view it inline below 👇

### Page 1
![Event Flow Page 1](./event_flow_page1.png)

### Page 2
![Event Flow Page 2](./event_flow_page2.png)

### Page 3
![Event Flow Page 3](./event_flow_page3.png)

### Page 4
![Event Flow Page 4](./event_flow_page4.png)

### Page 5
![Event Flow Page 5](./event_flow_page5.png)

### Page 6
![Event Flow Page 6](./event_flow_page6.png)

### Page 7
![Event Flow Page 7](./event_flow_page7.png)

### Page 8
![Event Flow Page 8](./event_flow_page8.png)

### Page 9
![Event Flow Page 9](./event_flow_page9.png)

### Page 10
![Event Flow Page 10](./event_flow_page10.png)

