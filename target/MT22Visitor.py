# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declarationlist.
    def visitDeclarationlist(self, ctx:MT22Parser.DeclarationlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declarationlisttail.
    def visitDeclarationlisttail(self, ctx:MT22Parser.DeclarationlisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolean.
    def visitBoolean(self, ctx:MT22Parser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#comment.
    def visitComment(self, ctx:MT22Parser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomicType.
    def visitAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensiontail.
    def visitDimensiontail(self, ctx:MT22Parser.DimensiontailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayType.
    def visitArrayType(self, ctx:MT22Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#voidType.
    def visitVoidType(self, ctx:MT22Parser.VoidTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#autoType.
    def visitAutoType(self, ctx:MT22Parser.AutoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idtail.
    def visitIdtail(self, ctx:MT22Parser.IdtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclnosemi.
    def visitVardeclnosemi(self, ctx:MT22Parser.VardeclnosemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecllist.
    def visitVardecllist(self, ctx:MT22Parser.VardecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecllisttail.
    def visitVardecllisttail(self, ctx:MT22Parser.VardecllisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para.
    def visitPara(self, ctx:MT22Parser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paralist.
    def visitParalist(self, ctx:MT22Parser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paratail.
    def visitParatail(self, ctx:MT22Parser.ParatailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcpropo.
    def visitFuncpropo(self, ctx:MT22Parser.FuncpropoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcbody.
    def visitFuncbody(self, ctx:MT22Parser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callexpr.
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idxOp.
    def visitIdxOp(self, ctx:MT22Parser.IdxOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlisttail.
    def visitExprlisttail(self, ctx:MT22Parser.ExprlisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#numOperand.
    def visitNumOperand(self, ctx:MT22Parser.NumOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#booleanOperand.
    def visitBooleanOperand(self, ctx:MT22Parser.BooleanOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringOperand.
    def visitStringOperand(self, ctx:MT22Parser.StringOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalOperand.
    def visitRelationalOperand(self, ctx:MT22Parser.RelationalOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtlisttail.
    def visitStmtlisttail(self, ctx:MT22Parser.StmtlisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_whilestmt.
    def visitDo_whilestmt(self, ctx:MT22Parser.Do_whilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockcontent.
    def visitBlockcontent(self, ctx:MT22Parser.BlockcontentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockcontentlist.
    def visitBlockcontentlist(self, ctx:MT22Parser.BlockcontentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockcontentlisttail.
    def visitBlockcontentlisttail(self, ctx:MT22Parser.BlockcontentlisttailContext):
        return self.visitChildren(ctx)



del MT22Parser