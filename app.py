import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd

# ========== 页面配置 ===========
st.set_page_config(
    page_title="AI Excel智能处理器 | 企业版",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== 自定义CSS ==========
st.markdown("""
<style>
    /* 全局样式 */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* 主标题 */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    /* 卡片样式 */
    .card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }

    /* 按钮样式 */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
    }

    /* 进度条样式 */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #4CC9F0, #4361EE);
    }

    /* 文件上传区域 */
    .upload-area {
        border: 3px dashed #4361EE;
        border-radius: 20px;
        padding: 4rem;
        text-align: center;
        background: rgba(67, 97, 238, 0.05);
        margin: 2rem 0;
    }

    /* 表格样式 */
    .dataframe {
        border: none !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border-radius: 10px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ========== 侧边栏导航 ==========
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1791/1791328.png", width=100)

    selected = option_menu(
        menu_title="导航菜单",
        options=["🏠 首页", "📁 文件处理", "📊 数据分析", "⚙️ 设置"],
        icons=['house', 'file-earmark-arrow-up', 'bar-chart', 'gear'],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa"},
            "icon": {"color": "orange", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#4361EE"},
        }
    )

# ========== 主页面内容 ==========
if selected == "🏠 首页":
    render_home_page()
elif selected == "📁 文件处理":
    render_file_processing()
elif selected == "📊 数据分析":
    render_data_analysis()
else:
    render_settings()


def render_home_page():
    """首页"""
    st.markdown('<h1 class="main-title">🤖 AI Excel智能处理器</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">企业级Excel数据智能处理平台</p>',
                unsafe_allow_html=True)

    # 特性展示
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>🎯 智能处理</h3>
            <p>用自然语言描述需求，AI自动生成处理代码</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>⚡ 快速高效</h3>
            <p>支持大文件分块处理，优化性能</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>📊 丰富可视化</h3>
            <p>自动生成图表和数据分析报告</p>
        </div>
        """, unsafe_allow_html=True)

    # 快速开始
    st.markdown("## 🚀 快速开始")

    with st.expander("点击查看使用指南", expanded=True):
        steps = [
            "1. **上传Excel文件** - 支持 .xlsx, .xls 格式",
            "2. **描述处理需求** - 用自然语言告诉AI要做什么",
            "3. **AI智能处理** - 自动生成并执行代码",
            "4. **查看结果** - 下载处理后的文件和报告"
        ]

        for step in steps:
            st.write(step)


def render_file_processing():
    """文件处理页面"""
    st.markdown("## 📁 智能文件处理")

    # 文件上传区域
    st.markdown('<div class="upload-area">', unsafe_allow_html=True)
    st.markdown("### 📤 拖放文件到这里")
    st.markdown("<p style='color: #666;'>支持 .xlsx, .xls 格式 • 最大200MB</p>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "选择文件",
        type=['xlsx', 'xls'],
        label_visibility="collapsed"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file:
        # 显示文件信息
        file_info_col1, file_info_col2, file_info_col3 = st.columns(3)

        with file_info_col1:
            st.metric("文件名", uploaded_file.name)
        with file_info_col2:
            st.metric("文件大小", f"{uploaded_file.size / 1024 / 1024:.1f} MB")
        with file_info_col3:
            st.metric("状态", "✅ 已上传")

        # 读取数据
        try:
            df = pd.read_excel(uploaded_file)

            # 数据预览
            st.markdown("### 📊 数据预览")
            st.dataframe(df.head(), use_container_width=True)

            # 处理需求
            st.markdown("### 📝 处理需求")

            # 需求模板
            template_col1, template_col2 = st.columns(2)

            with template_col1:
                if st.button("添加年薪列", use_container_width=True):
                    st.session_state.user_request = "添加'年薪'列，计算规则：工资×12"

                if st.button("数据筛选", use_container_width=True):
                    st.session_state.user_request = "筛选出销售额大于10000的记录"

            with template_col2:
                if st.button("分组统计", use_container_width=True):
                    st.session_state.user_request = "按部门分组计算平均工资"

                if st.button("数据清洗", use_container_width=True):
                    st.session_state.user_request = "删除重复行，填充缺失值"

            # 自定义需求
            user_request = st.text_area(
                "或输入自定义需求：",
                value=st.session_state.get('user_request', ''),
                height=100,
                placeholder="例如：添加'绩效奖金'列，计算规则：工资×0.3"
            )

            # 处理按钮
            if st.button("🚀 开始AI智能处理", type="primary", use_container_width=True):
                with st.spinner("AI正在分析处理..."):
                    # 模拟处理过程
                    progress_bar = st.progress(0)

                    for i in range(100):
                        time.sleep(0.02)
                        progress_bar.progress(i + 1)

                    # 简单处理示例
                    if '工资' in df.columns:
                        df['年薪'] = df['工资'] * 12

                    st.success("✅ 处理完成！")

                    # 显示结果
                    st.markdown("### 📈 处理结果")
                    st.dataframe(df, use_container_width=True)

                    # 生成图表
                    st.markdown("### 📊 数据可视化")

                    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
                    if numeric_cols:
                        selected_col = st.selectbox("选择要可视化的列", numeric_cols)

                        if selected_col:
                            fig = px.histogram(df, x=selected_col, title=f"{selected_col} 分布")
                            st.plotly_chart(fig, use_container_width=True)

                    # 下载按钮
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 下载处理结果(CSV)",
                        data=csv,
                        file_name="processed_data.csv",
                        mime="text/csv",
                        use_container_width=True
                    )

        except Exception as e:
            st.error(f"读取文件失败: {str(e)}")


def render_data_analysis():
    """数据分析页面"""
    st.markdown("## 📊 智能数据分析")

    # 生成示例数据
    np.random.seed(42)
    sample_data = pd.DataFrame({
        '月份': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        '销售额': np.random.randint(10000, 50000, 6),
        '利润': np.random.randint(2000, 10000, 6),
        '客户数': np.random.randint(50, 200, 6)
    })

    # 数据显示
    st.dataframe(sample_data, use_container_width=True)

    # 图表展示
    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(sample_data, x='月份', y='销售额', title='月度销售额')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.line(sample_data, x='月份', y=['销售额', '利润'], title='销售与利润趋势')
        st.plotly_chart(fig2, use_container_width=True)

    # AI分析报告
    st.markdown("### 🤖 AI分析报告")

    with st.expander("查看详细分析报告"):
        st.markdown("""
        ## 📋 数据分析报告

        ### 🔍 关键发现
        1. **销售趋势**：3月份销售额达到峰值
        2. **利润分析**：利润率稳定在20-25%之间
        3. **客户增长**：客户数逐月增长

        ### 🎯 建议
        - 加大3月份的营销投入
        - 优化成本控制，提高利润率
        - 加强客户关系管理

        ### 📈 预测
        预计下个季度销售额增长15-20%
        """)


def render_settings():
    """设置页面"""
    st.markdown("## ⚙️ 系统设置")

    setting_tab1, setting_tab2 = st.tabs(["基本设置", "高级设置"])

    with setting_tab1:
        st.markdown("### 🔧 基本配置")

        # AI模型选择
        model = st.selectbox(
            "AI模型选择",
            ["DeepSeek-V3 (推荐)", "GPT-4 Turbo", "Claude-3", "本地模型"]
        )

        # 处理模式
        processing_mode = st.radio(
            "处理模式",
            ["⚡ 快速模式", "🎯 精确模式", "🔒 安全模式"],
            horizontal=True
        )

        # 文件大小限制
        max_size = st.slider("最大文件大小(MB)", 10, 500, 200)

    with setting_tab2:
        st.markdown("### 🚀 高级配置")

        # 并行处理
        parallel = st.checkbox("启用并行处理", value=True)

        if parallel:
            workers = st.slider("并行任务数", 1, 10, 4)

        # 缓存设置
        cache = st.checkbox("启用结果缓存", value=True)


if __name__ == "__main__":
    import time
    import numpy as np

    render_file_processing()