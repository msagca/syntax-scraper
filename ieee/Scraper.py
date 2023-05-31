# -*- coding: utf-8 -*-

if __name__ is not None and "." in __name__:
    from .bnfParser import bnfParser
    from .bnfParserVisitor import bnfParserVisitor
else:
    from bnfParser import bnfParser
    from bnfParserVisitor import bnfParserVisitor


class Scraper(bnfParserVisitor):
    def __init__(self):
        super().__init__()
        self.hier_level = 0
        self.tokens = set()

    def visit(self, tree):
        return tree.accept(self)

    def visitChildren(self, node):
        text = ""
        n = node.getChildCount()
        for i in range(n):
            if i > 0:
                text += " "
            c = node.getChild(i)
            result = c.accept(self)
            if result == None:
                return "'Error!'"
            text += result
        if not text:
            return "'Error!'"
        return text

    def visitTerminal(self, node):
        return node.getText()

    def getLexerRules(self):
        char_names = {
            '"': "DQ",
            "-": "MI",
            ",": "CO",
            ";": "SC",
            ":": "CL",
            "!": "EM",
            "?": "QM",
            ".": "DT",
            "'": "AP",
            "(": "LP",
            ")": "RP",
            "[": "LB",
            "]": "RB",
            "{": "LC",
            "}": "RC",
            "@": "AT",
            "*": "AS",
            "/": "SL",
            "\\": "BS",
            "&": "AM",
            "#": "HA",
            "%": "MO",
            "`": "GA",
            "^": "CA",
            "+": "PL",
            "<": "LT",
            "=": "EQ",
            ">": "GT",
            "|": "VL",
            "~": "TI",
            "$": "DL",
            "0": "ZERO",
            "1": "ONE",
            "2": "TWO",
            "3": "THREE",
            "4": "FOUR",
            "5": "FIVE",
            "6": "SIX",
            "7": "SEVEN",
            "8": "EIGHT",
            "9": "NINE",
        }
        text = ""
        for token in sorted(self.tokens):
            rule_name = ""
            for char in token:
                if char in char_names:
                    rule_name += char_names[char]
                else:
                    rule_name += char.upper()
            text += f"\n{rule_name} : '{token}' ;"
        text += "\nCOMMENT : ( BLOCK_COMMENT | ONE_LINE_COMMENT ) -> channel(HIDDEN) ;\nIDENTIFIER : [a-zA-Z] [a-zA-Z0-9_]* ;\nSTRING_LITERAL : '\"' ( ~[\\r\\n\"\\\\] | '\\\\' [nt\\\\\"] )* '\"' ;\nUNSIGNED_NUMBER : [1-9] [0-9]* ;\nWHITE_SPACE : [ \\t\\r\\n]+ -> skip ;\nfragment BLOCK_COMMENT : '/*' .*? '*/' ;\nfragment ONE_LINE_COMMENT : '//' ~[\\r\\n]* ;"
        return text

    def visitFormal_syntax(self, ctx: bnfParser.Formal_syntaxContext):
        text = ""
        for rule in ctx.rule_definition():
            text += f"\n{self.visit(rule)}"
        return text

    def visitRule_definition(self, ctx: bnfParser.Rule_definitionContext):
        return f"{self.visit(ctx.rule_identifier())}\n\t: {self.visit(ctx.rule_alternatives())}\n\t;"

    def visitRule_alternatives(self, ctx: bnfParser.Rule_alternativesContext):
        if self.hier_level == 0:
            text = ""
            for i, alt in enumerate(ctx.alternative()):
                if i > 0:
                    text += "\n\t| "
                text += self.visit(alt)
            return text
        else:
            return self.visitChildren(ctx)

    def visitAlternative(self, ctx: bnfParser.AlternativeContext):
        return self.visitChildren(ctx)

    def visitItem(self, ctx: bnfParser.ItemContext):
        return self.visitChildren(ctx)

    def visitOptional_item(self, ctx: bnfParser.Optional_itemContext):
        self.hier_level += 1
        text = self.visit(ctx.rule_alternatives())
        left_index, right_index = ctx.getSourceInterval()
        if right_index - left_index > 2:
            text = f"( {text} )"
        text += "?"
        self.hier_level -= 1
        return text

    def visitRepeated_item(self, ctx: bnfParser.Repeated_itemContext):
        self.hier_level += 1
        text = self.visit(ctx.rule_alternatives())
        left_index, right_index = ctx.getSourceInterval()
        if right_index - left_index > 2:
            text = f"( {text} )"
        text += "*"
        self.hier_level -= 1
        return text

    def visitRule_identifier(self, ctx: bnfParser.Rule_identifierContext):
        return self.visit(ctx.IDENTIFIER())

    def visitRule_reference(self, ctx: bnfParser.Rule_referenceContext):
        return self.visit(ctx.IDENTIFIER())

    def visitKeyword_or_punctuation(self, ctx: bnfParser.Keyword_or_punctuationContext):
        text = self.visit(ctx.STRING_TEXT())
        self.tokens.add(text)
        return f"'{text}'"
