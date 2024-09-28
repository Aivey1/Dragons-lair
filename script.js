let memeImage = document.getElementById('memeImage');
let interval;
let position = 0;

function startMoving() {
    document.getElementById('startBtn').disabled = true;
    document.getElementById('stopBtn').disabled = false;

    interval = setInterval(function() {
        position += 5;
        memeImage.style.left = position + 'px';
    }, 100);
}

function stopMoving() {
    document.getElementById('startBtn').disabled = false;
    document.getElementById('stopBtn').disabled = true;

    clearInterval(interval);
}
