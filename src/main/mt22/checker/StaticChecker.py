from ast import Dict
from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC
        
class Pair():
    def __init__(self, name, type):
        self.name  = name
        self.type = type

class ParameterType():
    def __init__(self, name, type, inherit = False, out = False):
        self.name  = name
        self.type = type
        self.inherit = inherit
        self.out = out
        
        
    
# Add a new type
class NumType(Type):pass
#Function will be an object that have dictionary of list of parameter  
class FuncType(Type):
    def __init__(self, parameters, returnType=VoidType(), inherit = False):
        self.parameters = parameters
        self.returnType = returnType
        self.inherit = inherit

class GetEnv(Visitor):
    def __init__(self):
        pass
        
    def visitProgram(self,ctx:Program,o:object): 
        o = []
        for decl in ctx.decls:
            if(isinstance(decl, FuncDecl)):
                self.visit(decl, o)
        special_function= [
            Pair("readInteger",FuncType(parameters=[],returnType=IntegerType())),
            Pair("printInteger",FuncType(parameters=[ParameterType('arg',IntegerType())],returnType= VoidType())),
            Pair("readFloat",FuncType(parameters=[], returnType=FloatType())),
            Pair("writeFloat",FuncType(parameters=[ParameterType('arg',FloatType())],returnType= VoidType())),
            Pair("readBoolean",FuncType(parameters=[], returnType=BooleanType())),
            Pair("printBoolean",FuncType(parameters=[ParameterType('arg',BooleanType())],returnType= VoidType())),
            Pair("readString",FuncType(parameters=[], returnType=StringType())),
            Pair("printString",FuncType(parameters=[ParameterType('arg',StringType())],returnType= VoidType()))
        ]
        o = o + special_function
        return o
 
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        env = {}
        if ctx.name in o:
            raise Redeclared( Function ,ctx.name)
        env = []
        for param in ctx.params:
            env = self.visit(param, env) 
        # if(len(ctx.params) == 0):
        o += [Pair(ctx.name, FuncType(env, ctx.return_type, ctx.inherit))]
        return o

    def visitParamDecl(self,ctx:ParamDecl,o:object):
        name = ctx.name
        type = ctx.typ
        out = ctx.out
        inherit = ctx.inherit
        for para in o:
            if(para.name == name):
                raise Redeclared(Parameter(),name)
        o.append(ParameterType(name, type, inherit, out))
        return o
        # return o [parameter1, parameter2, ...]
        

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visitProgram(self.ast, [])
    
    
    
    #Check the type
    def visitIntegerType(self, ast, param): 
        return IntegerType()
    def visitFloatType(self, ast, param): 
        return FloatType()
    def visitBooleanType(self, ast, param): 
        return BooleanType()
    def visitStringType(self, ast, param): 
        return StringType()
    def visitArrayType(self, ast, param): 
        return ArrayType(ast.dimensions, ast.typ)
    def visitAutoType(self, ast, param): 
        return AutoType()
    def visitVoidType(self, ast, param): 
        return VoidType()
    
    
    
    #Check Expression
    
   #BinExpr will return type of the expresion (IntegerType, FloatType, BooleanType, StringType) Numtype for Int or Float
    def visitBinExpr(self, ast, param): 
        op = ast.op
        #Left and Right will the type
        typeleft = ast.left
        typeright = ast.right
        
        if(isinstance(typeleft,Id)):
            left, idxleft = self.visit(typeleft, param)
        elif(isinstance(typeleft, BinExpr)):
            left = self.visit(typeleft, param)
        elif(isinstance(typeleft, FuncCall)):
            left, idxleft = self.visit(typeleft, param)
        else: left = typeleft
        if(isinstance(typeright,Id)):
            right, idxright = self.visit(typeright, param)
        elif(isinstance(typeright, BinExpr)):
            right = self.visit(typeright, param)
        elif(isinstance(typeright,FuncCall)):
            right, idxright = self.visit(typeright, param)
        else: right = typeright
        returnType = 0
        #Arithmetic operator
        if(op in ['+', '-', '*', '/']):
            # print(isinstance(left, (IntegerType,FloatType, AutoType)))
            if(isinstance(left, (IntegerLit,IntegerType,FloatLit,FloatType, NumType, AutoType)) and isinstance(right, (IntegerLit,IntegerType,FloatLit,FloatType,NumType, AutoType)) ):
                if(isinstance(left, (IntegerLit,IntegerType,AutoType)) and isinstance(right,(IntegerLit,IntegerType,AutoType))):
                    returnType = IntegerType()
                    if(isinstance(left, AutoType) and isinstance(right, AutoType)):
                        pass
                    else:
                        if(isinstance(left, AutoType)):
                            if(isinstance(typeleft,Id)):
                                param[idxleft[0]][idxleft[1]].type = IntegerType()
                            elif(isinstance(typeleft, FuncCall)):
                                param[len(param) - 1][idxleft].type.returnType = IntegerType()
                        elif(isinstance(right, AutoType)):
                            if(isinstance(typeright,Id)):
                                param[idxright[0]][idxright[1]].type = IntegerType()
                            elif(isinstance(typeright, FuncCall)):
                                param[len(param) - 1][idxright].type.returnType = IntegerType()
                            
                    return returnType                
                elif(isinstance(left, (FloatLit,FloatType,NumType,AutoType)) or isinstance(left, (FloatLit,FloatType,NumType,AutoType))):
                    returnType = FloatType()
                    if(isinstance(left, AutoType) and isinstance(right, AutoType)):
                        pass
                    else:
                        if(isinstance(left, AutoType)):
                            if(isinstance(typeleft,Id)):
                                param[idxleft[0]][idxleft[1]].type = FloatType()
                            elif(isinstance(typeleft, FuncCall)):
                                param[len(param) - 1][idxleft].type.returnType = FloatType()
                        elif(isinstance(right, AutoType)):
                            if(isinstance(typeright,Id)):
                                param[idxright[0]][idxright[1]].type = FloatType()
                            elif(isinstance(typeright, FuncCall)):
                                param[len(param) - 1][idxright].type.returnType = FloatType()
                    return returnType
            raise TypeMismatchInExpression(ast)
        if(op in ['%']):
            if(isinstance(left, (IntegerLit,IntegerType,NumType,AutoType)) and isinstance(right,(IntegerLit,IntegerType,NumType,AutoType))):
                returnType = IntegerType()
                if(isinstance(left, AutoType) and isinstance(right, AutoType)):
                    pass
                else:
                    if(isinstance(left, AutoType)):
                        if(isinstance(typeleft,Id)):
                            param[idxleft[0]][idxleft[1]].type = IntegerType()
                        elif(isinstance(typeleft, FuncCall)):
                            param[len(param) - 1][idxleft].type.returnType = IntegerType()
                    elif(isinstance(right, AutoType)):
                        if(isinstance(typeright,Id)):
                            param[idxright[0]][idxright[1]].type = IntegerType()
                        elif(isinstance(typeright, FuncCall)):
                            param[len(param) - 1][idxright].type.returnType = IntegerType()
                return returnType                
            raise TypeMismatchInExpression(ast)
        
        #Relational
        if(op in ['>', '>=', '<', '<=']):
            # print(isinstance(left, (IntegerType,FloatType, AutoType)))
            if(isinstance(left, (IntegerLit,IntegerType,FloatLit,FloatType,NumType, AutoType)) and isinstance(right, (IntegerLit,IntegerType,FloatLit,FloatType,NumType,AutoType)) ):
                if(isinstance(left, (IntegerLit,IntegerType,NumType,AutoType)) and isinstance(right,(IntegerLit,IntegerType,NumType,AutoType))):
                    returnType = BooleanType()
                    if(isinstance(left, AutoType) and isinstance(right, AutoType)):
                        pass
                    else:
                        if(isinstance(left, AutoType)):
                            if(isinstance(typeleft,Id)):
                                param[idxleft[0]][idxleft[1]].type = IntegerType()
                            elif(isinstance(typeleft, FuncCall)):
                                param[len(param) - 1][idxleft].type.returnType = IntegerType()
                        elif(isinstance(right, AutoType)):
                            if(isinstance(typeright,Id)):
                                param[idxright[0]][idxright[1]].type = IntegerType()
                            elif(isinstance(typeright, FuncCall)):
                                param[len(param) - 1][idxright].type.returnType = IntegerType()
                    return returnType                
                elif(isinstance(left, (FloatLit,FloatType,NumType,AutoType)) or isinstance(left, (FloatLit,FloatType,NumType,AutoType))):
                    returnType = BooleanType()
                    if(isinstance(left, AutoType) and isinstance(right, AutoType)):
                        pass
                    else:
                        if(isinstance(left, AutoType)):
                            if(isinstance(typeleft,Id)):
                                param[idxleft[0]][idxleft[1]].type = FloatType()
                            elif(isinstance(typeleft, FuncCall)):
                                param[len(param) - 1][idxleft].type.returnType = FloatType()
                        elif(isinstance(right, AutoType)):
                            if(isinstance(typeright,Id)):
                                param[idxright[0]][idxright[1]].type = FloatType()
                            elif(isinstance(typeright, FuncCall)):
                                param[len(param) - 1][idxright].type.returnType = FloatType()
            raise TypeMismatchInExpression(ast)
        if(op in ['==', '!=']):
            # print(isinstance(left, (IntegerType,FloatType, AutoType)))
            if(isinstance(left, (IntegerLit,IntegerType,BooleanLit,BooleanType,NumType,AutoType)) and isinstance(right, (IntegerLit,IntegerType,BooleanLit,BooleanType,NumType,AutoType))):
                if(isinstance(left, (IntegerLit,IntegerType,NumType,AutoType)) and isinstance(right,(IntegerLit,IntegerType,NumType,AutoType))):
                    returnType = BooleanType()
                    if(isinstance(left, AutoType) and isinstance(right, AutoType)):
                        pass
                    else:
                        if(isinstance(left, AutoType)):
                            if(isinstance(typeleft,Id)):
                                param[idxleft[0]][idxleft[1]].type = IntegerType()
                            elif(isinstance(typeleft, FuncCall)):
                                param[len(param) - 1][idxleft].type.returnType = IntegerType()
                        elif(isinstance(right, AutoType)):
                            if(isinstance(typeright,Id)):
                                param[idxright[0]][idxright[1]].type = IntegerType()
                            elif(isinstance(typeright, FuncCall)):
                                param[len(param) - 1][idxright].type.returnType = IntegerType()
                    return returnType                
                elif(isinstance(left, (BooleanLit,BooleanType,AutoType)) or isinstance(left, (BooleanLit,BooleanType,AutoType))):
                    returnType = BooleanType()
                    if(isinstance(left, AutoType) and isinstance(right, AutoType)):
                        pass
                    else:
                        if(isinstance(left, AutoType)):
                            if(isinstance(typeleft,Id)):
                                param[idxleft[0]][idxleft[1]].type = BooleanType()
                            elif(isinstance(typeleft, FuncCall)):
                                param[len(param) - 1][idxleft].type = BooleanType()
                        elif(isinstance(right, AutoType)):
                            if(isinstance(typeright,Id)):
                                param[idxright[0]][idxright[1]].type = BooleanType()
                            elif(isinstance(typeright, FuncCall)):
                                param[len(param) - 1][idxright].type.returnType = BooleanType()
                    return returnType
                elif(isinstance(left, (BooleanLit,BooleanType, IntegerLit, IntegerType)) and isinstance(right, (BooleanLit,BooleanType, IntegerLit, IntegerType))  ):
                    returnType = BooleanType()
                    return returnType
            raise TypeMismatchInExpression(ast)
        
        #Logical
        if(op in ['&&', '||']):
            if(isinstance(left, (BooleanLit,BooleanType,AutoType)) and isinstance(right,(BooleanLit,BooleanType,AutoType))):
                returnType = BooleanType()
                if(isinstance(left, AutoType) and isinstance(right, AutoType)):
                    pass
                else:
                    if(isinstance(left, AutoType)):
                        if(isinstance(typeleft,Id)):
                            param[idxleft[0]][idxleft[1]].type = BooleanType()
                        elif(isinstance(typeleft, FuncCall)):
                            param[len(param) - 1][idxleft].type.returnType = BooleanType()
                    elif(isinstance(right, AutoType)):
                        if(isinstance(typeright,Id)):
                            param[idxright[0]][idxright[1]].type = BooleanType()
                        elif(isinstance(typeright, FuncCall)):
                            param[len(param) - 1][idxright].type.returnType = BooleanType()
                return returnType                
            raise TypeMismatchInExpression(ast)
            
        if(op in ['::']):
            if(isinstance(left, (StringType,StringLit,AutoType)) and isinstance(right,(StringLit,StringType,AutoType))):
                returnType = StringType()
                if(isinstance(left, AutoType) and isinstance(right, AutoType)):
                    pass
                else:
                    if(isinstance(left, AutoType)):
                        if(isinstance(typeleft,Id)):
                            param[idxleft[0]][idxleft[1]].type = StringType()
                        elif(isinstance(typeleft, FuncCall)):
                            param[len(param) - 1][idxleft].type.returnType = StringType()
                    elif(isinstance(right, AutoType)):
                        if(isinstance(typeright,Id)):
                            param[idxright[0]][idxright[1]].type = StringType()
                        elif(isinstance(typeright, FuncCall)):
                            param[len(param) - 1][idxright].type.returnType = StringType()
                return returnType                
            raise TypeMismatchInExpression(ast)
        pass
    

    def visitUnExpr(self, ast, param): 
        op = ast.op
        type = ast.val
        if(isinstance(type,Id)):
            left, idx = self.visit(type, param)
        elif(isinstance(type,(IntegerLit, FloatLit, StringLit,BooleanLit))):
            left = self.visit(type, param)
        elif(isinstance(type,FuncCall)):
            left, idx = self.visit(type, param)
        else: left = type
        # print(left)
        if(op in '-'):
            if(isinstance(left,(IntegerType, FloatType ,NumType, AutoType))):
                if(isinstance(left, IntegerType)):
                    return IntegerType()
                elif(isinstance(left, FloatType)):
                    return FloatType()
                elif(isinstance(left,NumType)):
                    return NumType()
                elif(isinstance(left, AutoType)):
                    if(isinstance(type,Id)):
                        param[idx[0]][idx[1]].type = AutoType()
                    elif(isinstance(type, FuncCall)):
                        param[len(param) - 1][idx].type.returnType = AutoType()
                return NumType()
            raise TypeMismatchInExpression(ast)
        elif(op in '!'):
            if(isinstance(left,(BooleanType, AutoType))):
                if(isinstance(left, AutoType)):
                    if(isinstance(type,Id)):
                        param[idx[0]][idx[1]].type = BooleanType()
                    elif(isinstance(type, FuncCall)):
                        param[len(param) - 1][idx].type.returnType = BooleanType()
                return BooleanType()
            raise TypeMismatchInExpression(ast) 
        pass
    
    #Return the type of id and its idx in the list 
    def visitId(self, ast, param): 
        name = ast.name
        for i,env in enumerate(param):
            for j,pair in enumerate(env):
                if name in pair.name:
                    if(isinstance(pair.type, FuncType)):
                        continue
                    return pair.type, [i, j] 
        raise Undeclared(Identifier(), name)   

    def visitArrayCell(self, ast, param): 
        #param will be a list of local environment
        name = ast.name
        found = False
        ## Check if such a name exist and its type
        for env in param:
            for el in env:
                if(el.name == name):
                    typ = el.type
                    found = True
                    break    
        if(not found): raise TypeMismatchInExpression(ast)
        else: 
            if(not isinstance(typ, ArrayType)):
                raise TypeMismatchInExpression(ast)
        #Check length, if larger dimension => raise error
        celldimen = len( ast.cell )
        if(type(typ.dimensions) is not List):
            typ.dimensions = [typ.dimensions]
        arrdimen = len(typ.dimensions)
        if(celldimen > arrdimen):
            raise TypeMismatchInExpression(ast)
        print(name, typ)
        
        #Check expr, if not interger then raise error
        for expr in ast.cell:
            if(isinstance(expr, Id)):
                exprtyp, idx = self.visit(expr, param)
            elif(isinstance(expr, FuncCall)):
                exprtyp, idx = self.visit(expr, param)
            else: exprtyp = self.visit(expr, param)
            if(isinstance(exprtyp, AutoType)):
                if(isinstance(expr, Id)):
                    param[idx[0]][idx[1]] = IntegerType()
                    exprtyp = IntegerType()
                elif(isinstance(expr, FuncCall)):
                    param[len(param) - 1][idx].type.returnType = IntegerType()
                    exprtyp = IntegerType()
            
            if(not isinstance(exprtyp, IntegerType)):
                raise TypeMismatchInExpression(ast) 
            
            
        #Return array atomic type:
        returnType = typ.typ
        return returnType
    
    def visitIntegerLit(self, ast, param): 
        return IntegerType()
    def visitFloatLit(self, ast, param): 
        return FloatType()
    def visitStringLit(self, ast, param): 
        return StringType()
    def visitBooleanLit(self, ast, param): 
        return BooleanType()
    #Return type of arraylit and number of parameter in arrayLit
    def visitArrayLit(self, ast, param): 
        #param will contains 2-tuple (localenv: param, List[int]: dim)
        #we need to return param, type, list[int]
        localenv = param[0]
        dim = param[1]
        exprlist = ast.explist
        # print(exprlist)
        if(isinstance(exprlist[0], ArrayLit)):
            localenv, typeofarraylit, numofchildfirst = self.visit(exprlist[0], (localenv,dim))    
            dim+= [numofchildfirst]
            for numofexpr, expr in enumerate(exprlist):
                # print(expr, dim)
                localenv, typ, numofchild = self.visit(expr, (localenv,dim))
                if(numofchild != numofchildfirst):
                    raise IllegalArrayLiteral(ast)
                if(not(type(typ) is type(typeofarraylit))):
                    raise IllegalArrayLiteral(ast)
            dim += [numofexpr + 1] 
            return localenv,typeofarraylit, dim
        else:
            for expr in exprlist:
                if(isinstance(expr, Id)):
                    typeofarraylit, idxfirst = self.visit(expr, localenv)
                elif(isinstance(expr, FuncCall)):
                    typeofarraylit, idxfirst = self.visit(expr, localenv)
                else: typeofarraylit = self.visit(expr, localenv)
                if(not isinstance(typeofarraylit,AutoType)): 
                    break
            for numofexpr,expr in enumerate(exprlist):
                if(isinstance(expr, Id)):
                    exprtyp, idx = self.visit(expr, localenv)
                elif(isinstance(expr, FuncCall)):
                    exprtyp, idx = self.visit(expr, localenv)
                else: exprtyp = self.visit(expr, localenv)
                    
                if(isinstance(exprtyp, AutoType)):
                    if(isinstance(expr, Id)):
                        localenv[idx[0]][idx[1]] = typeofarraylit
                    elif(isinstance(expr, FuncCall)):
                        localenv[len(localenv) - 1][idx].type.returnType = typeofarraylit
                elif(isinstance(exprtyp, IntegerType) and isinstance(typeofarraylit, FloatType)):
                    pass
                elif(not(type(exprtyp) is type(typeofarraylit))):
                    raise IllegalArrayLiteral(ast)
            dim = numofexpr + 1
            # print('inthisloop', dim)
            return localenv,typeofarraylit, dim
        
    
    
    
    
    ##Check this expr again , return functype and idx of that call function
    def visitFuncCall(self, ast, param): 
        #Check if such function exist
        found = False
        for i,func in enumerate(param[len(param) - 1]):
            if(func.name == ast.name):
                localfunc = func
                found = True
                funcidx = i
                break
        if(not(found)): raise Undeclared(Function(), ast.name)
        
        #Get the parameter list of such function and create argument list
        paralist = localfunc.type.parameters
        # paralist = [Parameter1, Parameter2, ..]
        count = len(ast.args)
        if(count != len(paralist)):
            raise TypeMismatchInExpression(ast)
        for i,expr in enumerate(ast.args):
            ##Check the type of the argument
            if(isinstance(expr, Id)):
                typ, idx = self.visit(expr, param)
            elif(isinstance(expr, FuncCall)):
                typ, idx = self.visit(expr, param)
            else: typ = self.visit(expr, param) 
            
            # print(expr, ' type of argument',typ, ' type of parameter', paralist[i].type)
            ##Compare the type of argument and parameter
            # Parameter is auto type
            if(isinstance(paralist[i].type, AutoType)):
                paralist[i].type = typ
            # Argument is auto type
            elif(isinstance(typ, AutoType)):
                if(isinstance(expr, Id)):
                    param[idx[0]][idx[1]].type = paralist[i].type 
                elif(isinstance(expr, FuncCall)):
                    param[len(param) - 1][idx].type.returnType = paralist[i].type
            elif(isinstance(paralist[i].type, FloatType) and isinstance(typ,IntegerType)):
                pass
            elif(type(paralist[i].type) is not type(typ)):
                raise TypeMismatchInExpression(ast)
        
        
        #Update list of parameter back to function
        param[len(param) - 1][funcidx].type.parameters = paralist
        
        return  localfunc.type.returnType, funcidx



    #Check statements
    def visitAssignStmt(self, ast, param): 
        typeoflhs = ast.lhs
        typeofrhs = ast.rhs
        localenv = param[0]
        # print(localenv)
        if(isinstance(typeoflhs, Id)):
            lhs, idxl = self.visit(typeoflhs, localenv)
        else: lhs = self.visit(typeoflhs, localenv)
        if(isinstance(lhs,(VoidType, ArrayType))):
            raise TypeMismatchInStatement(ast)
        if(isinstance(typeofrhs, Id)):
            rhs, idxr = self.visit(typeofrhs, localenv)
        elif(isinstance(typeofrhs, FuncCall)):
            rhs, idxr = self.visit(typeofrhs, localenv)
        else: rhs = self.visit(typeofrhs, localenv)
        # print(lhs, rhs)
        if(isinstance(rhs,(VoidType, ArrayType))):
            raise TypeMismatchInStatement(ast)
        elif(isinstance(lhs, AutoType)):
            localenv[idxl[0]][idxl[1]].type = rhs
        elif(isinstance(typeofrhs, FuncCall)):
            if(isinstance(rhs, AutoType)):
                localenv[len(localenv) - 1][idxr].type.returnType = lhs
        elif(isinstance(lhs, FloatType) and isinstance(rhs,IntegerType)):
            pass
        elif(not(type(lhs) is type(rhs))):
            raise TypeMismatchInStatement(ast)
        return (localenv, param[1], param[2])
        
    def visitBlockStmt(self, ast, param): 
        #param will consist of a tuple (list: localenv, int: inLoop, int: funcidx )
        
        #Local environment will have another inside scope to store it variable
        body = ast.body
        localenv = [[]] + param[0] 
        inLoop = param[1]
        funcidx = param[2]
        
        
        ##Visit all statement in blockstmt body
        ##As this is stmt, state of multiple varible will change
        ## WE WILL UPDATE THE CHANGE IN THE LOCAL ENVIRONMENT FIRST
        ## THEN RE-ASSIGN IT BACK TO OUR GLOBAL ENVIRONMENT (param)
        for el in body:
            if(isinstance(el,VarDecl)):
                localenv = self.visit(el, localenv)
            elif(isinstance(el, ReturnStmt)):
                localenv,inLoop, funcidx = self.visit(el, (localenv, inLoop, funcidx))
                break
            else:
                localenv,inLoop, funcidx = self.visit(el, (localenv, inLoop, funcidx))
        
        
        ## Assign back to param the current environment, drop the latest scope
        param = localenv[1:]
        return (param, inLoop, funcidx)
    
    def visitIfStmt(self, ast, param): 
        localenv = param[0]
        typeofcond = ast.cond 
        if(isinstance(typeofcond, Id)):
            cond, idx = self.visit(typeofcond, localenv)
        elif(isinstance(typeofcond, FuncCall)):
            cond, idx = self.visit(typeofcond, localenv)
        else: cond = self.visit(typeofcond, localenv)
        if(not(isinstance(cond, BooleanType))):
            raise TypeMismatchInStatement(ast)
        
        #Check whether true statement, false statement are (Breakstmt,ContinueStmt) or not
        localparam = (localenv, param[1], param[2])
        localparam = self.visit(ast.tstmt, localparam)
        localparam = self.visit(ast.fstmt, localparam)
        return localparam
    
    def visitForStmt(self, ast, param): #LOOP
        localenv = param[0]
        inLoopinit = param[1] 

        localenv, inLoopinit, funcidx  = self.visit(ast.init, (localenv,param[1], param[2]))
        #Check type of condition, if not boolean then raise errors
        typeofcond = ast.cond 
        if(isinstance(typeofcond, Id)):
            cond, idxcond = self.visit(typeofcond, localenv)
        elif(isinstance(typeofcond, FuncCall)):
            cond, idxcond = self.visit(typeofcond, localenv)
        else:
            cond = self.visit(typeofcond, localenv)
        if(not(isinstance(cond, BooleanType))):
            raise TypeMismatchInStatement(ast)
        
        #Check type of update, if not integer then raise errors
        typeofupd = ast.upd 
        if(isinstance(typeofupd, Id)):
            upd, idxupd = self.visit(typeofupd, localenv)
        elif(isinstance(typeofupd, FuncCall)):
            upd, idxupd = self.visit(typeofupd, localenv)
        else: upd = self.visit(typeofupd, localenv)
        if(not(isinstance(upd, IntegerType))):
            raise TypeMismatchInStatement(ast)
        
        
        inLoop = param[1] + 1
        localparam = (localenv, inLoop, param[2])
        localparam = self.visit(ast.stmt, localparam)
        if(inLoop == localparam[1]):
            localparam = (localparam[0], localparam[1] - 1, localparam[2])
        return localparam
        
    def visitWhileStmt(self, ast, param): #LOOP
        #Check type of condition, if not boolean then raise errors
        localenv = param[0]
        typeofcond = ast.cond 
        if(isinstance(typeofcond, Id)):
            cond, idx = self.visit(typeofcond, localenv)
        elif(isinstance(typeofcond, FuncCall)):
            cond, idx = self.visit(typeofcond, localenv)
        else: cond = self.visit(typeofcond, localenv)
        if(not(isinstance(cond, BooleanType))):
            raise TypeMismatchInStatement(ast)
        
        inLoop = param[1] + 1
        localparam = (localenv, inLoop, param[2])
        localparam = self.visit(ast.stmt, localparam)
        if(inLoop == localparam[1]):
            localparam = (localparam[0], localparam[1] - 1, localparam[2])
        return localparam
        
    def visitDoWhileStmt(self, ast, param): #LOOP
        #Check type of condition, if not boolean then raise errors
        inLoop = param[1] + 1 
        localparam = (param[0], inLoop, param[2])
        localparam = self.visit(ast.stmt, localparam)
        if(inLoop == localparam[1]):
            localparam = (localparam[0], localparam[1] - 1, localparam[2])
        localenv = localparam[0] 
        typeofcond = ast.cond 
        if(isinstance(typeofcond, Id)):
            cond, idx = self.visit(typeofcond, localenv)
        elif(isinstance(typeofcond, FuncCall)):
            cond, idx = self.visit(typeofcond, localenv)
        else: cond = self.visit(typeofcond, localenv)
        if(not(isinstance(cond, BooleanType))):
            raise TypeMismatchInStatement(ast)
        return localparam
        
    def visitBreakStmt(self, ast, param): 
        if(param[1] <= 0):
            return MustInLoop(ast)
        else:
            inLoop = param[1] - 1
            return (param[0], inLoop, param[2]) 
    
    def visitContinueStmt(self, ast, param):
        if(param[1] <=  0):
            return MustInLoop(ast)
        else:
            inLoop = param[1] - 1
            return (param[0], inLoop, param[2]) 
    
    #Return type of expression or voidtype
    def visitReturnStmt(self, ast, param): 
        funcidx = param[2]
        localenv = param[0]
        if(ast.expr is None):
            typ = VoidType()
        else:
            expr = ast.expr
            if(isinstance(expr, Id)):
                typ, idx = self.visit(expr, localenv)
            elif(isinstance(expr, FuncCall)):
                typ, idx = self.visit(expr, localenv)
            else: typ = self.visit(expr, localenv)
        funcReturnType = localenv[len(localenv) - 1][funcidx].type.returnType
        if(isinstance(funcReturnType, AutoType)):
            localenv[len(localenv) - 1][funcidx].type.returnType = typ
        elif(type(funcReturnType) is not type(typ)):
            raise TypeMismatchInStatement(ast)
        return (localenv, param[1], funcidx)

      
    #The same with FuncCall, just dont return any type or argument    
    def visitCallStmt(self, ast, param): 
        #Check if such function exist
        localenv = param[0]
        found = False
        for i,func in enumerate(localenv[len(localenv) - 1]):
            if(func.name == ast.name):
                localfunc = func
                found = True
                funcidx = i
                break
        if(not(found)): raise Undeclared(Function(), ast.name)
        #Get the parameter list of such function and create argument list
        paralist = localfunc.type.parameters
        # paralist = [Parameter1, Parameter2, ..]
        count = len(ast.args)
        if(count != len(paralist)):
            raise TypeMismatchInStatement(ast)
        for i,expr in enumerate(ast.args):
            ##Check the type of the argument
            if(isinstance(expr, Id)):
                typ, idx = self.visit(expr, localenv)
            elif(isinstance(expr, FuncCall)):
                typ, idx = self.visit(expr, localenv)
            else: typ = self.visit(expr, localenv) 
            
            # print(expr, ' type of argument',typ, ' type of parameter', paralist[i].type)
            ##Compare the type of argument and parameter
            # Parameter is auto type
            if(isinstance(paralist[i].type, AutoType)):
                paralist[i].type = typ
            # Argument is auto type
            elif(isinstance(typ, AutoType)):
                if(isinstance(expr, Id)):
                    localenv[idx[0]][idx[1]].type = paralist[i].type 
                elif(isinstance(expr, FuncCall)):
                    localenv[len(localenv) - 1][idx].type.returnType = paralist[i].type
            elif(isinstance(paralist[i].type, FloatType) and isinstance(typ,IntegerType)):
                pass
            elif(type(paralist[i].type) is not type(typ)):
                raise TypeMismatchInStatement(ast)
        
        
        #Update list of parameter back to function
        localenv[len(localenv) - 1][funcidx].type.parameters = paralist
        
        #if function returntype is AutoType, change it to VoidType
        if(isinstance(localfunc.type.returnType, AutoType)):
            localenv[len(localenv) - 1][funcidx].type.returnType = VoidType
        
        return (localenv, param[1], param[2])
        



    #Check declarations
    def visitVarDecl(self, ast, param): 
        name = ast.name
        typeofvar = ast.typ
        
        for pair in param[0]: 
            if name in pair.name:
                raise Redeclared(Variable(), name) 
        
        # Append the pair in to the list
        pair = [Pair(name, typeofvar)]
        param[0] = param[0] + pair 
        #Init will be 0 if None and a type if expression
        init = 0


        
        if(ast.init is not None and ast.init is not ArrayLit):    
            if(isinstance(ast.init, Id)):
                typeofinit, idx = self.visit(ast.init, param)
            elif(isinstance(ast.init, FuncCall)):
                typeofinit, idx = self.visit(ast.init, param)
            elif(isinstance(ast.init, ArrayLit)):
                arrlitdimen = []
                param, typeofinit, arrlitdimen = self.visit(ast.init, (param,arrlitdimen))
            else: typeofinit = self.visit(ast.init ,param)
        ## Init is arrayType
        if(isinstance(typeofvar, (ArrayType, AutoType)) and isinstance(ast.init, ArrayLit)):
            if(isinstance(typeofvar, ArrayType)):    
                if(not isinstance(ast.init, ArrayLit)):
                    raise Invalid(Variable(), name)

                typvardimen = list(map(lambda x: int(x), typeofvar.dimensions))
                # print(typvardimen)
                if(type(arrlitdimen) != list):
                    arrlitdimen = [arrlitdimen]
                arrlitdimen = arrlitdimen[::-1]
                #Check if these 2 have same dimen
                boolsamedimen = True
                if(len(typvardimen) != len(arrlitdimen)):
                    boolsamedimen = False
                for i in range(0, len(typvardimen)):
                     if(typvardimen[i] != arrlitdimen[i]):
                          boolsamedimen = False
                if(type(typeofinit) is type(typeofvar.typ) and boolsamedimen):
                    pass
                else:
                    raise TypeMismatchInVarDecl(ast)
            elif(isinstance(typeofvar, AutoType)):
                if(isinstance(ast.init, ArrayLit)):
                    typeofvar = ArrayType(arrlitdimen, typeofinit)
            
        else:
            if(isinstance(ast.init, ArrayLit)):
                raise Invalid(Variable(),name)
        
       
            
            
        #Auto type without init
        if(isinstance(typeofvar,AutoType) and ast.init is None):
            raise Invalid(Variable(), name)
        #Auto type with init
        elif(isinstance(typeofvar,AutoType)):
            typeofvar = typeofinit

        
        
        #Init is autoType
        if(ast.init is not None):
            if(isinstance(typeofinit, AutoType)):
                if(isinstance(ast.init, Id)):
                    param[idx[0]][idx[1]].type = typeofvar 
                elif(isinstance(ast.init, FuncCall)):
                    param[len(param) - 1][idx].type.returnType = typeofvar
            elif(isinstance(typeofvar, FloatType) and isinstance(typeofinit, IntegerType)):
                pass
            elif(type(typeofvar) is not type(typeofinit) and not isinstance(ast.init,ArrayLit)):
                raise TypeMismatchInVarDecl(ast)

        
        # Append the pair in to the list
        for pair in param[0]: 
            for pairname in pair.name:
                if(name == pairname):
                    pair.type = typeofvar
        return param
        
        
    def visitParamDecl(self, ast, param):
        pass
        
    def visitFuncDecl(self, ast, param): 
        #Update the param with new function
        for i, func in enumerate(param[len(param) - 1]):
            if(ast.name == func.name):
                localfunc = func
                funcidx = i
                break
        param[0] = param[0] + [localfunc]
        
        # Get parameter out and checking if parent function is declared:
        localParameter = localfunc.type.parameters
        inheritParameter = []
        found = False
        if(ast.inherit == None):
            found = True
        if(ast.inherit is not None):    
            for j,func in enumerate(param[len(param) - 1]):
                if(ast.inherit == func.name):
                    found = True
                    inheritParameter =  list(filter(lambda x: (x.inherit == True),func.type.parameters))
                    parentfuncidx = j
                    break
        if(not(found)): raise Undeclared(Function(), ast.inherit )        
        
            
            
        for para in localParameter:
            for inheritpara in inheritParameter:
                # print(para.name, inheritpara.name)
                if(para.name == inheritpara.name):
                    raise Invalid(Parameter(), para.name)
        parameter = localParameter + inheritParameter
        # pairpara = list(map(lambda x: Pair(x.name, x.type), parameter))
        
            
        #Update the local environment 
        localenv = [parameter]
        localenv = localenv + param
        # print('before', localenv)
        
        #Check the first stmt
        if(ast.inherit is not None):
            parentfunction = localenv[len(localenv) - 1][parentfuncidx]
            firststmt = ast.body.body[0]
            if(len(parentfunction.type.parameters) == 0):
                if(firststmt.name == "preventDefault"):
                    ast.body.body = ast.body.body[1:]
                else: 
                    name = localenv[len(localenv) - 1][parentfuncidx].name
                    args = []
                    firststmtfuncall = CallStmt(name, args )
                    idx = 0
                    inloop = 0
                    localenv, inloop, idx =  self.visit(firststmtfuncall, (localenv,inloop, idx))              
            else:
                if(isinstance(firststmt, CallStmt)):
                    if(firststmt.name == "super"):
                        name = localenv[len(localenv) - 1][parentfuncidx].name
                        args = firststmt.args
                        # print(name)
                        firststmtfuncall = CallStmt(name, args )
                        inloop = 0
                        idx = 0
                        # print(firststmtfuncall)
                        localenv, inloop, idx =  self.visit(firststmtfuncall, (localenv,inloop, idx))
                        ast.body.body = ast.body.body[1:]
                    elif(firststmt.name == "preventDefault"):
                        ast.body.body = ast.body.body[1:]
                else: raise InvalidStatementInFunction(firststmt)
        
        
        #Visit body using localenv
        inLoop = 0
        localenv, inLoop, funcidx = self.visit(ast.body, (localenv, inLoop, funcidx ))
        # print('after', localenv)
        
        # # #Update local parameter and inherit parameter based on local environment:
        for para in localParameter:
            for localpara in localenv[0]:
                if(para.name == localpara.name):
                    para.type = localpara.type
        localfunc.type.parameters = localParameter
        param[len(param) - 1][funcidx] = localfunc
            
        if(not(ast.inherit == None)):        
            for para in param[len(param) - 1][parentfuncidx].type.parameters:
                for localpara in localenv[0]:
                    if(para.name == localpara.name):
                        para.type = localpara.type
        
        return param


 
    #check program
    def visitProgram(self, ast, param): 
        env = [[]]
        firsttime = GetEnv().visit(ast, param)
        env.append(firsttime)
        decls = ast.decls
        
        # print("before")
        # for func in env[1]:
        #     print( func.name, func.type.returnType )
        #     for para in func.type.parameters: 
        #         print(para.name, para.type) 
        # print('\n\n')
        
        for decl in decls:
            param = self.visit(decl, env) #return a param that contain all the current identifiers and functions

        # print("after")
        # for env in param[len(param) - 1]:
        #     print( env.name, env.type.returnType )
        #     for para in env.type.parameters: 
        #         print(para.name, para.type) 
        
        main = False    
        for func in param[len(param) - 1]:
            if(func.name == "main" and type(func.type.returnType) is VoidType):
                main = True
                break
            
        if(not(main)): raise NoEntryPoint()   
        return
