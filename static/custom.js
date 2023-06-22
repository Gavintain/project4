$(document).ready(function() {
    var isDragging = false;
    var startPosition;
    var startOffset;

    $(".bottom-section").mousedown(function(e) {
        isDragging = true;
        startPosition = e.clientY;
        startOffset = $(this).offset().top;
        $(this).addClass("dragging");
    });

    $(document).mousemove(function(e) {
        if (isDragging) {
            var offsetY = e.clientY - startPosition;
            $(".bottom-section").css("top", startOffset + offsetY);
        }
    });

    $(document).mouseup(function() {
        if (isDragging) {
            isDragging = false;
            $(".bottom-section").removeClass("dragging");
        }
    });
});