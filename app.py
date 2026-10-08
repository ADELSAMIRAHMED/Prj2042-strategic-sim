import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# SOL-1002.25: AI Strategic Decision Web Application
st.set_page_col_config(page_title="PRJ2042 - AI Strategic Simulator", layout="wide")

# عنوان الموقع الاحترافي
st.title("🛡️ AI Strategic Decision Model & Visualizer (SOL-1002.25)")
st.markdown("### Project 2042 - Dynamic Optimization Framework")
st.write("---")

# تقسيم الصفحة إلى نصفين: يسار للمدخلات، ويمين للنتائج والرسومات
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("📋 Step 1: Input Tactical Data")
    
    # مدخلات قواتنا
    st.markdown("**Our Forces (Country A)**")
    my_jets = st.number_input("Our Fighter Jets ✈️", min_value=0, value=10)
    my_tanks = st.number_input("Our Modern Tanks 🚜", min_value=0, value=50)
    my_def = st.number_input("Our Air Defense 🛡️", min_value=0, value=1)
    
    # مدخلات الأعداء
    st.markdown("**Enemy Forces (Country B)**")
    en_jets = st.number_input("Enemy Fighter Jets ✈️", min_value=0, value=12)
    en_tanks = st.number_input("Enemy Modern Tanks 🚜", min_value=0, value=70)
    en_def = st.number_input("Enemy Air Defense 🛡️", min_value=0, value=3)
    
    # الميزانية
    st.markdown("**Strategic Variables**")
    budget = st.number_input("Available Budget ($M)", min_value=0.0, value=500.0)

    # زر تشغيل الذكاء الاصطناعي
    run_simulation = st.button("⚡ Execute AI Optimization Loops", type="primary")

with col2:
    st.subheader("📊 Step 2: AI Optimized Recommendation")
    
    if run_simulation:
        costs = {'jets': 80.0, 'tanks': 8.0, 'defense': 150.0}
        remaining_budget = budget
        
        # حساب الفجوات لترتيب أولويات الشراء الذكي لحماية الأمن القومي
        gap_jets = max(0, en_jets - my_jets)
        gap_tanks = max(0, en_tanks - my_tanks)
        
        final_jets, final_tanks, final_defense = 0, 0, 0
        
        # نظام التخصيص المالي الصارم (المحفظة الذكية المتتالية)
        if gap_jets > 0 and my_def < 5:
            needed_def = min(3, int(remaining_budget // costs['defense']))
            final_defense += needed_def
            remaining_budget -= (needed_def * costs['defense'])
            
        if gap_tanks > 0 and remaining_budget >= costs['tanks']:
            affordable_tanks = int(remaining_budget // costs['tanks'])
            bought_tanks = min(gap_tanks, affordable_tanks)
            final_tanks += bought_tanks
            remaining_budget -= (bought_tanks * costs['tanks'])
            
        if remaining_budget >= costs['jets']:
            affordable_jets = int(remaining_budget // costs['jets'])
            final_jets += affordable_jets
            remaining_budget -= (affordable_jets * costs['jets'])
            
        if remaining_budget >= costs['tanks']:
            extra_tanks = int(remaining_budget // costs['tanks'])
            final_tanks += extra_tanks
            remaining_budget -= (extra_tanks * costs['tanks'])

        c_j = final_jets * 80
        c_t = final_tanks * 8
        c_d = final_defense * 150
        total_spent = c_j + c_t + c_d
        rem = budget - total_spent
        
        # عرض التقرير المالي بشكل فخم وجداول مصفوفة
        st.success("🎯 Training and Optimization Completed Successfully!")
        
        report_df = pd.DataFrame({
            'Strategic Asset': ['Fighter Jets ✈️', 'Modern Tanks 🚜', 'Air Defense 🛡️'],
            'Quantity To Buy': [final_jets, final_tanks, final_defense],
            'Total Cost ($M)': [c_j, c_t, c_d]
        })
        st.dataframe(report_df, use_container_width=True)
        
        st.metric(label="Total Invested Capital", value=f"${total_spent:.0f}M")
        st.metric(label="Remaining Cash Reserves", value=f"${rem:.0f}M")
        
        # رسم وتحديث البيان الدائري الديناميكي فوراً
        labels = ['Jets', 'Tanks', 'Air Defense', 'Cash']
        sizes = [c_j, c_t, c_d, rem]
        colors = ['#3182ce', '#dd6b20', '#319795', '#cbd5e0']
        
        f_labels = [labels[i] for i in range(4) if sizes[i] > 0]
        f_sizes = [sizes[i] for i in range(4) if sizes[i] > 0]
        f_colors = [colors[i] for i in range(4) if sizes[i] > 0]
        
        if f_sizes:
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.pie(f_sizes, labels=f_labels, autopct='%1.1f%%', startangle=140, colors=f_colors, textprops=dict(weight="bold"))
            ax.set_title("AI Tactical Capital Allocation", fontsize=12, weight="bold", color="#1a365d")
            st.pyplot(fig)
    else:
        st.info("Adjust the parameters on the left and click 'Execute AI Optimization Loops' to generate the strategic model.")
