from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.declarationlist()))
    
    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        if(ctx.vardecl() is not None):
            return self.visit(ctx.vardecl())
        else:
            return [self.visit(ctx.funcdecl())]

    # Visit a parse tree produced by MT22Parser#declarationlist.
    def visitDeclarationlist(self, ctx:MT22Parser.DeclarationlistContext):
        if(ctx.getChildCount() != 2):
            return self.visit(ctx.declaration())
        else:
            return self.visit(ctx.declaration()) + self.visit(ctx.declarationlisttail())
             

    # Visit a parse tree produced by MT22Parser#declarationlisttail.
    def visitDeclarationlisttail(self, ctx:MT22Parser.DeclarationlisttailContext):
        if(ctx.getChildCount() != 2):
            return []
        else:
            return self.visit(ctx.declaration()) + self.visit(ctx.declarationlisttail())
            
    # Visit a parse tree produced by MT22Parser#boolean.
    def visitBoolean(self, ctx:MT22Parser.BooleanContext):
        return BooleanLit(True if (ctx.TRUE() is not None) else False)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist()))

    # Visit a parse tree produced by MT22Parser#atomicType.
    def visitAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        if (ctx.INTEGER()):
            return IntegerType()
        elif (ctx.FLOAT()):
            return FloatType()
        elif (ctx.BOOLEAN()):
            return BooleanType()
        else: 
            return StringType()


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        if(ctx.dimensiontail() is None):
            return [(ctx.INTLIT().getText())]
        else:
            return [(ctx.INTLIT().getText())] + self.visit(ctx.dimensiontail())


    # Visit a parse tree produced by MT22Parser#dimensiontail.
    def visitDimensiontail(self, ctx:MT22Parser.DimensiontailContext):
        if (ctx.getChildCount() != 3):
            return []
        else: 
            return [(ctx.INTLIT().getText())] + self.visit(ctx.dimensiontail())


    # Visit a parse tree produced by MT22Parser#arrayType.
    def visitArrayType(self, ctx:MT22Parser.ArrayTypeContext):
        return ArrayType(self.visit(ctx.dimension()),self.visit(ctx.atomicType()))    


    # Visit a parse tree produced by MT22Parser#voidType.
    def visitVoidType(self, ctx:MT22Parser.VoidTypeContext):
        return VoidType()


    # Visit a parse tree produced by MT22Parser#autoType.
    def visitAutoType(self, ctx:MT22Parser.AutoTypeContext):
        return AutoType()


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        if(ctx.getChildCount() == 1):
            return [Id(ctx.ID().getText())]
        else:
            return [Id(ctx.ID().getText())] + self.visit(ctx.idtail()) 


    # Visit a parse tree produced by MT22Parser#idtail.
    def visitIdtail(self, ctx:MT22Parser.IdtailContext):
        if(ctx.getChildCount() != 3):
            return []
        else:
            return [Id(ctx.ID().getText())] + self.visit(ctx.idtail())

    
#####################################    
###### DE CUOI NHO LAM ############## 
#####################################   
    # S: a = b | R;
    # R: a = b| a, R , b
    #VarDecl(name, type, init(expr or none))
    # => This have to return a list of vardecl for each id in idlist
    
    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        if(ctx.vardeclnosemi() is None):
            idlist = self.visit(ctx.idlist())
            idtype = self.visit(ctx.getChild(2))
            return [VarDecl(x.name,idtype,None) for x in idlist] #Checking if the expr here is none or not
        else:
            idlist, vartype, exprlist = self.visit(ctx.vardeclnosemi())
            return  list(map(lambda x,y: VarDecl(x, vartype, y), idlist, exprlist))
        
    #return an IDlist, a vartype, and exprlist
    # Visit a parse tree produced by MT22Parser#vardeclnosemi.
    def visitVardeclnosemi(self, ctx:MT22Parser.VardeclnosemiContext):
        if(ctx.vardeclnosemi() is None):
            explist = self.visit(ctx.expr())
            return [ctx.ID().getText()], self.visit(ctx.getChild(2)), self.visit(ctx.expr()) if (type(explist) is list) else [explist]
        else:
            idlist, vartype, exprlist = self.visit(ctx.vardeclnosemi())
            explist = self.visit(ctx.expr())
            return  [ctx.ID().getText()] + idlist, vartype, (exprlist + explist) if (type(explist) is list) else (exprlist + [explist])  
    
#####################################    
###### DE CUOI NHO LAM ############## 
#####################################  

    # Visit a parse tree produced by MT22Parser#para.
    def visitPara(self, ctx:MT22Parser.ParaContext):
        type = 0
        if(ctx.atomicType() is not None):
            type = self.visit(ctx.atomicType())
        elif(ctx.autoType() is not None):
            type = self.visit(ctx.autoType())
        elif(ctx.dimension() is not None):
            type = self.visit(ctx.dimension())
        else: 
            type = self.visit(ctx.arrayType())
        return ParamDecl(ctx.ID().getText(), type, bool(ctx.OUT() is not None), bool(ctx.INHERIT() is not None))


    # Visit a parse tree produced by MT22Parser#paralist.
    def visitParalist(self, ctx:MT22Parser.ParalistContext):
        if(ctx.paratail() is None):
            return [self.visit(ctx.para())]
        else:
            return [self.visit(ctx.para())] + self.visit(ctx.paratail())


    # Visit a parse tree produced by MT22Parser#paratail.
    def visitParatail(self, ctx:MT22Parser.ParatailContext):
        if(ctx.para() is None):
            return []
        else:
            return [self.visit(ctx.para())] + self.visit(ctx.paratail())



    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        name, return_type, params, inherit = self.visit(ctx.funcpropo())
        block = self.visit(ctx.funcbody())
        return FuncDecl(name,return_type, params, inherit, block)

    # Visit a parse tree produced by MT22Parser#funcpropo.
    def visitFuncpropo(self, ctx:MT22Parser.FuncpropoContext):
        paralist = []
        if (ctx.paralist() is not None):
            paralist = self.visit(ctx.paralist()) 
        return ctx.ID()[0].getText(), self.visit(ctx.getChild(3)), paralist, None if (ctx.INHERIT() is None) else (ctx.ID()[1].getText())


    # Visit a parse tree produced by MT22Parser#funcbody.
    def visitFuncbody(self, ctx:MT22Parser.FuncbodyContext):
        return self.visit(ctx.blockstmt())


    # Visit a parse tree produced by MT22Parser#callexpr.
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        exprlist = []
        if(ctx.exprlist() is not None):
            exprlist = self.visit(ctx.exprlist())
        return FuncCall(ctx.ID().getText(), exprlist )


    # Visit a parse tree produced by MT22Parser#idxOp.
    def visitIdxOp(self, ctx:MT22Parser.IdxOpContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.exprlist()))


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if (ctx.getChildCount() == 3):
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if (ctx.getChildCount() == 3):
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if (ctx.getChildCount() == 3):
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if (ctx.getChildCount() == 3):
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if (ctx.getChildCount() == 3):
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if (ctx.getChildCount() == 2):
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if (ctx.getChildCount() == 2):
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if (ctx.idxOp() is not None):
            return self.visit(ctx.idxOp())
        else:
            return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        if (ctx.ID() is not None):
            return Id(ctx.ID().getText())
        elif (ctx.numOperand() is not None):
            return self.visit(ctx.getChild(0))
        elif (ctx.booleanOperand() is not None):
            return self.visit(ctx.getChild(0))
        elif (ctx.stringOperand() is not None):
            return self.visit(ctx.getChild(0))
        elif (ctx.relationalOperand() is not None):
            return self.visit(ctx.getChild(0))
        elif (ctx.callexpr() is not None):
            return self.visit(ctx.getChild(0))
        elif (ctx.subexpr() is not None):
            return self.visit(ctx.getChild(0))
        else:
            return self.visit(ctx.getChild(0))
        


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        if(ctx.getChildCount() == 1):
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprlisttail())
        
    # Visit a parse tree produced by MT22Parser#exprlisttail.
    def visitExprlisttail(self, ctx:MT22Parser.ExprlisttailContext):
        if(ctx.expr() is None):
            return []
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprlisttail())



    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MT22Parser#numOperand.
    def visitNumOperand(self, ctx:MT22Parser.NumOperandContext):
        if (ctx.INTLIT() is not None):
            return IntegerLit(int(ctx.INTLIT().getText()))
        else: 
            if(ctx.FLOATLIT().getText().startswith('.')):
                newfloat = '0' + ctx.FLOATLIT().getText()
                return FloatLit(float(newfloat))
            else:
                return FloatLit(float(ctx.FLOATLIT().getText()))


    # Visit a parse tree produced by MT22Parser#booleanOperand.
    def visitBooleanOperand(self, ctx:MT22Parser.BooleanOperandContext):
        return self.visit(ctx.boolean())


    # Visit a parse tree produced by MT22Parser#stringOperand.
    def visitStringOperand(self, ctx:MT22Parser.StringOperandContext):
        return StringLit(ctx.STRLIT().getText())


    # Visit a parse tree produced by MT22Parser#relationalOperand.
    def visitRelationalOperand(self, ctx:MT22Parser.RelationalOperandContext):
        if(ctx.INTLIT() is not None):
            return IntegerLit(int(ctx.INTLIT().getText()))
        else:
            return self.visit(ctx.boolean())


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if (ctx.assignstmt() is not None):
            return self.visit(ctx.assignstmt())
        elif (ctx.ifstmt() is not None):
            return self.visit(ctx.ifstmt())
        elif (ctx.forstmt() is not None):
            return self.visit(ctx.forstmt())
        elif (ctx.whilestmt() is not None):
            return self.visit(ctx.whilestmt())
        elif (ctx.do_whilestmt() is not None):
            return self.visit(ctx.do_whilestmt())
        elif (ctx.breakstmt() is not None):
            return self.visit(ctx.breakstmt())
        elif (ctx.continuestmt() is not None):
            return self.visit(ctx.continuestmt())
        elif (ctx.returnstmt() is not None):
            return self.visit(ctx.returnstmt())
        elif (ctx.callstmt() is not None):
            return self.visit(ctx.callstmt())
        else:
            return self.visit(ctx.blockstmt())


    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        if(ctx.getChildCount() == 1):
            return [self.visit(ctx.stmt())]
        else:
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlisttail())


    # Visit a parse tree produced by MT22Parser#stmtlisttail.
    def visitStmtlisttail(self, ctx:MT22Parser.StmtlisttailContext):
        if(ctx.getChildCount() != 2):
            return []
        else:
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlisttail())

    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if(ctx.ID() is not None):
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.idxOp())

    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        fstmt = None
        if (ctx.ELSE() is not None):
            fstmt = self.visit(ctx.stmt()[1])
        return IfStmt(self.visit(ctx.expr()),self.visit(ctx.getChild(4)),fstmt)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        assignstmt = AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()[0]))
        return ForStmt(assignstmt,self.visit(ctx.expr()[1]),self.visit(ctx.expr()[2]),self.visit(ctx.stmt()) )


    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))


    # Visit a parse tree produced by MT22Parser#do_whilestmt.
    def visitDo_whilestmt(self, ctx:MT22Parser.Do_whilestmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockstmt()))

    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        returnstmt = None
        if(ctx.expr() is not None):
            returnstmt = self.visit(ctx.expr())
        return ReturnStmt(returnstmt)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        name = (ctx.ID().getText())
        exprlist = []
        if(ctx.exprlist() is not None):
            exprlist = self.visit(ctx.exprlist())
        return CallStmt(name, exprlist)


    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        blockcontentlist = []
        if(ctx.blockcontentlist() is not None):
            blockcontentlist = self.visit(ctx.blockcontentlist())
        return BlockStmt(blockcontentlist)

    # Visit a parse tree produced by MT22Parser#blockcontent.
    def visitBlockcontent(self, ctx:MT22Parser.BlockcontentContext):
        if(ctx.stmt() is not None):
            return self.visit(ctx.stmt())
        else: return self.visit(ctx.vardecl())


    # Visit a parse tree produced by MT22Parser#blockcontentlist.
    def visitBlockcontentlist(self, ctx:MT22Parser.BlockcontentlistContext):
        if (ctx.getChildCount() != 2):
            content = self.visit(ctx.blockcontent()) 
            return content if (type(content)is list) else [content]
        else:
            content = self.visit(ctx.blockcontent()) 
            if(type(content) is list):
                return content + self.visit(ctx.blockcontentlisttail())
            else:
                return [self.visit(ctx.blockcontent())] + self.visit(ctx.blockcontentlisttail())


    # Visit a parse tree produced by MT22Parser#blockcontentlisttail.
    def visitBlockcontentlisttail(self, ctx:MT22Parser.BlockcontentlisttailContext):
        if (ctx.getChildCount() != 2):
            return []
        else:
            content = self.visit(ctx.blockcontent()) 
            if(type(content) is list):
                return content + self.visit(ctx.blockcontentlisttail())
            else:
                return [self.visit(ctx.blockcontent())] + self.visit(ctx.blockcontentlisttail())
