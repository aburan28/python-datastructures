
























def depthFirst(startingNode, soughtValue):
   visitedNodes = set()
   stack = [startingNode]

   while len(stack) > 0:
      node = stack.pop()
      if node in visitedNodes:
         continue

      visitedNodes.add(node)
      if node.value == soughtValue:
         return True

      for n in node.adjacentNodes:
         if n not in visitedNodes:
            stack.append(n)
   return False