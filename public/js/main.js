window.onload = function () {
    const socket = io('localhost:8080');

    function sendMessage() {
        const token = 'TOKEN!!!';
        const message = document.getElementById('message').value;
        socket.emit('sendMessage', { token, message });
    }

    function subscribeRoom(room) {
        const token = 'TOKEN!!!';
        socket.emit('subscribeChat', { token, room });
    }

    function onSendMessage(data) {
        console.log(data);
    }
    document.getElementById('sendMessage').addEventListener('click', sendMessage);
    document.getElementById('subscribeChat1').addEventListener('click', () =>
        subscribeRoom('subscribeChat1')
    );
    document.getElementById('subscribeChat2').addEventListener('click', () =>
        subscribeRoom('subscribeChat2')
    );

    socket.on('connect', () => {});
    socket.on('sendMessage', onSendMessage);
}
