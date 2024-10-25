from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Node  # Assuming you have a Node model defined

class RuleFormView(APIView):
    def get(self, request):
        return render(request, 'api/rule_form.html')

class RuleEngine(APIView):
    
    def create_rule(self, rule_string):
        # Parse the rule_string and create an AST
        root = Node(node_type="operator", value="AND")  # Placeholder for actual logic
        return root  # Return the root of the AST


    
    def combine_rules(self, rules):
        combined_ast = Node(node_type="operator", value="OR")  # Combine using OR
        current = combined_ast
        for rule in rules:
            ast = self.create_rule(rule)
            # Link AST nodes
            if current.left is None:
                current.left = ast
            else:
                current.right = ast  # Simplified for demonstration
        return combined_ast

    def evaluate_rule(self, ast, data):
        if ast.node_type == "operand":
            return True  # Placeholder return
        elif ast.node_type == "operator":
            left_result = self.evaluate_rule(ast.left, data) if ast.left else True
            right_result = self.evaluate_rule(ast.right, data) if ast.right else True
            if ast.value == "AND":
                return left_result and right_result
            elif ast.value == "OR":
                return left_result or right_result
        return False

    def post(self, request):
        rule_string = request.data.get('rule_string')
        
        if rule_string:
            # Create a single rule
            try:
                ast = self.create_rule(rule_string)
                return Response({"message": "Rule created", "ast": ast.to_dict()}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            rules = request.data.get('rules')
            if rules and isinstance(rules, list):
                # Combine multiple rules
                try:
                    combined_ast = self.combine_rules(rules)
                    return Response({"message": "Rules combined", "ast": combined_ast.to_dict()}, status=status.HTTP_201_CREATED)
                except Exception as e:
                    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"error": "Rule string or rules list is required."}, status=status.HTTP_400_BAD_REQUEST)
