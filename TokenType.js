export class TokenType {
    constructor(name, regex) {
        this.name = name;
        this.regex = regex;
    }
}

export const tokenTypesList = {
    'NUMBER': new TokenType('NUMBER', /[0-9]+/gy),
    'VARIABLE': new TokenType('VARIABLE', /[а-я]+/gy),
    'SEMICOLON': new TokenType('SEMICOLON', /;/gy),
    'SPACE': new TokenType('SPACE', /\s/gy),
    'ASSIGN': new TokenType('ASSIGN', /=/gy),
    'LOG': new TokenType('LOG', /log/gy),
    'PLUS': new TokenType('PLUS', /+/gy),
    'MINUS': new TokenType('MINUS', /-/gy),
    'LPAR': new TokenType('LPAR', /\(/gy,
    'RPAR': new TokenType('RPAR', /\)/gy,
}
