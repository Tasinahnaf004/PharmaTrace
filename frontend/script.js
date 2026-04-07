<!DOCTYPE html>
<html>
<head>
    <title>IUB Chatbot</title>
    <style>
        body { font-family: Arial; background: #f0f0f0; padding: 20px; }
        #chatbox { width: 500px; margin: auto; padding: 20px; background: white; border-radius: 8px; }
        .message { margin: 10px 0; }
        .user { text-align: right; color: blue; }
        .bot { text-align: left; color: green; }
        input { padding: 5px; }
        button { padding: 5px 10px; }
    </style>
</head>

<body>
    <div id="chatbox">
        <h2>IUB Student Chatbot</h2>
        <div id="messages"></div>

        <input id="inputMsg" type="text" placeholder="Ask something..." style="width:80%;">
        <button id="sendBtn" onclick="sendMessage()">Send</button>
    </div>

    <script src="script.js"></script>
</body>
</html>
