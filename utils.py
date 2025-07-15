import streamlit as st

def render_palette(colors):
    # Custom CSS for beautiful color boxes
    st.markdown("""
        <style>
            .palette-container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 20px;
                margin-top: 20px;
            }
            .color-box {
                width: 70px;
                height: 70px;
                border-radius: 12px;
                border: 2px solid #ddd;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                transition: transform 0.2s;
            }
            .color-box:hover {
                transform: scale(1.1);
                cursor: pointer;
            }
            .color-label {
                text-align: center;
                margin-top: 8px;
                font-size: 13px;
                font-family: 'Courier New', monospace;
                color: #333;
            }
        </style>
    """, unsafe_allow_html=True)

    # Show the color palette
    st.markdown('<div class="palette-container">', unsafe_allow_html=True)
    for color in colors:
        st.markdown(f"""
            <div>
                <div class="color-box" style="background-color: {color};"></div>
                <div class="color-label">{color}</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
