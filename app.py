import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

# ========== 随机名字生成 ==========
def random_name():
    name_list = ["AI", "Zen", "Nova", "Echo", "Flux", "Aura", "Kai", "Mira", "Sol", "Vera"]
    return random.choice(name_list)

# ========== 随机渐变背景 ==========
def draw_gradient_background(ax, color1, color2):
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    ax.imshow(gradient, aspect='auto', cmap=None,
              extent=[0, 1, 0, 1],
              interpolation='bicubic')

    # 自定义渐变
    ax.imshow(np.linspace(0, 1, 256).reshape(1, -1),
              cmap=plt.get_cmap("viridis"),
              interpolation='bicubic')

# ========== Blob 生成函数 ==========
def generate_blob(ax, color, wobble):
    # 生成随机控制点
    theta = np.linspace(0, 2 * np.pi, 12)
    r = 0.3 + wobble * (np.random.rand(len(theta)) - 0.5)
    x = 0.5 + r * np.cos(theta)
    y = 0.5 + r * np.sin(theta)

    ax.fill(x, y, color=color, alpha=0.7)

# ========== 海报绘制 ==========
def draw_poster(palette, wobble, blob_count):
    fig, ax = plt.subplots(figsize=(6, 8))

    # 隐藏坐标轴
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # 颜色方案
    colors = {
        "Sunset": ["#FAD961", "#F76B1C", "#D83A56"],
        "Ocean": ["#1B98F5", "#2D46B9", "#154C79"],
        "Forest": ["#6A994E", "#386641", "#A7C957"],
        "Candy": ["#FF6F91", "#FFC1E3", "#FF9671"]
    }

    color_list = colors[palette]

    # 背景颜色（渐变暂时用纯色替代，确保兼容性）
    ax.set_facecolor(color_list[0])

    # 画 blobs
    for _ in range(blob_count):
        generate_blob(ax, random.choice(color_list[1:]), wobble)

    # 写名字
    ax.text(0.5, 0.08, random_name(), ha='center', fontsize=30, color="white")

    st.pyplot(fig)

# ========== Streamlit UI ==========
st.title("🎨 AI Poster Generator（静态版）")

st.sidebar.header("设置")

palette = st.sidebar.selectbox(
    "选择调色板 Palette",
    ["Sunset", "Ocean", "Forest", "Candy"]
)

wobble = st.sidebar.slider(
    "Wobble 抖动程度",
    0.0, 1.0, 0.3
)

blob_count = st.sidebar.slider(
    "Blob 数量",
    1, 10, 4
)

if st.button("✨ 生成海报"):
    draw_poster(palette, wobble, blob_count)
else:
    st.write("点击左侧选择参数，再按下按钮生成海报！")


