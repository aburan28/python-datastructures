

#include <stdio.h>
#include <stdlib.h>





dfs(graph *g, int v)
{
	edgenode *p;
	int y;
	if (finished) return;
	discovered[v] =TRUE;
	time = time + 1;
	entry_time[v] = time;

	process_vertex_early(v);

	p = g->edges[v];
	while (p != NULL) {
		y = p->y;
		if (discovered[y] == FALSE) {
			parent[y] = v;
			process_edge(v,y);
			dfs(g,y);
		}
		else if ((!processed[y] && (parent[v]! = y)) || (g->directed))
			process_edge(v,y);
		if (finished) return;
		p = p->next;

	}
	process_vertex_early(v);

	time = time + 1;
	exit_time[v] = time;

	processed[c] = TRUE;



}



int fibonacci_recursive(int n)
{
	if (n==0) return(0);
	if (n==1) return(1);

	return(fibonacci_recursive(n-1) + fibonacci_recursive(n-2));
}
pop_component(int v)
{
	int t;
	components_found = components_found + 1;
	scc[v] = components_found;
	while((t=pop(&active)) != v) {
		scc[t] = components_found;
	}
}
process_vertex_early(int v)
{
	push(&active, v);
}
strong_components(graph *g)
{
	/* pg 182 */
	int i;



}

process_vertex_late(int v)
{
	/* page 181 */
	push(&sorted,v);

}

edge_classification(int x, int y)
{




}



topsort(graph *g)
{
	int i; /* counter */
	init_stack(&sorted);
	for (i=1;i<=g->vertices;i++)
		if (discovered[i] == FALSE)
			dfs(g,i);


	print_stack(&sorted); /* report topological order */
}
process_edge(int x, int y){
	if (discovered[y] && (parent[x] != y)) {
		/* found a back edge */
		printf("Cycle from %d to $d:",y,x);
		find_path(y,x,parent);
		printf("\n\n");
		finished = TRUE;

	}
}







