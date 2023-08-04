Array.prototype.forEach = function(callback, context) {
    context = context || undefined;
    for (var i = 0; i < this.length; i++) {
        callback.call(context, this[i], i, this);
    }
}