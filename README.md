# GPU_Tf

If anyone faces the problem i was facing can implement the above lines of code. Tensorflow was not recognizing my Desired gpu gpu:1 and was Executing on Integrated GPU by default not even recognizing it.
One can the Activity of GPu while executing the code

Before Execution follow the steps for installation

1) Install <b>Python and add to path</b>
2) Install <b>Anaconda</b> and add to path but <b>dont set it as default python</b>
3) Create a Virtual Environment
   ```conda create -n vs_gpu python=3.10```
   ```conda activate vs_gpu```
   ```conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0```
   ```python -m pip install "tensorflow=2.10" "numpy==1.26.4"```

4) Test for your GPU if not detected then implement above lines of code
   
