import TokenType from "./TokenType";

export class Token {
    constructor(type, text, pos) {
        this.type = type;
        this.text = text;
        this.pos = pos;
    }

}
