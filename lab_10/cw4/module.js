class Operation {
    constructor(x, y) {
        /** Creating x and y in constructor */
        this.x = x;
        this.y = y;
    }
    sum() {
        /** adding two numbers and returning their values */
        return this.x + this.y;
    }

    show() {
        /** method to print result */
        console.log(`Suma wynosi ${this.sum()}`);
    }

};
/** exporting module */
export default Operation;