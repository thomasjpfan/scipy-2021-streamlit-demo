import streamlit as st

st.write("""## SciPy fft module!

`scipy.fft` *supports* dispatching to **CuPy**.

```python
x = cp.arange(10)
with scipy.fft.set_backend(cu_fft):
    y_cupy = scipy.fft.fft(x)
```

$$
X_k = \sum_{n=0}^{N-1} x_ne^{-i2\pi kn/N}
$$


- [Link to docs](https://docs.scpy.org/doc/scipy/reference/generated/scipy.fft.fft.html) for `scipy.fft.fft`
""")
