import Lexer from "./Lexer";
import Parser from "./Parser";

const code =
    `
    `

const lexer = new Lexer(code);

lexer.lexAnalysis()

const parser = new Parser(lexer.tokenList);

const rootNode = parser.parseCode()

parser.run(rootNode);
