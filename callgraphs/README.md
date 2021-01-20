
To create a callgraph with vtune, one can use [grpof2dot](https://github.com/jrfonseca/gprof2dot). Install with 
```
yum install python3 graphviz
pip install gprof2dot
``` 
Run a vtune hotspot analysis as usual. Then run something like: 
```
vtune -report gprof-cc -result-dir output -format text -report-output output.txt
gprof2dot -f axe output.txt | dot -Tpng -o output.png
``` 

The graph generated shows 
- total time % is the percentage of the running time spent in this function and all its children;
- self time % is the percentage of the running time spent in this function alone

In the default temperature-like color-map, functions where most time is spent (hot-spots) are marked as saturated red, and functions where little time is spent are marked as dark blue. Note that functions where negligible or no time is spent do not appear in the graph by default.
