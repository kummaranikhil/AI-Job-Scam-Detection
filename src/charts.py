import plotly.graph_objects as go


def probability_chart(fake_prob, real_prob):
    """
    Creates a bar chart showing prediction probabilities.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=["🟢 Genuine", "🔴 Fake"],
            y=[real_prob, fake_prob],
            text=[
                f"{real_prob:.2f}%",
                f"{fake_prob:.2f}%"
            ],
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Prediction Probability",
        xaxis_title="Prediction",
        yaxis_title="Probability (%)",
        yaxis=dict(range=[0, 100]),
        height=450,
        template="plotly_white"
    )

    return fig


def pie_chart(fake_prob, real_prob):
    """
    Creates a pie chart of prediction probabilities.
    """

    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Genuine", "Fake"],
                values=[real_prob, fake_prob],
                hole=0.45,
                textinfo="label+percent"
            )
        ]
    )

    fig.update_layout(
        title="Prediction Distribution",
        height=450,
        template="plotly_white"
    )

    return fig


def confidence_gauge(confidence):
    """
    Creates a gauge chart for model confidence.
    """

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=confidence,
            title={"text": "Model Confidence (%)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"thickness": 0.3},
                "steps": [
                    {"range": [0, 40]},
                    {"range": [40, 70]},
                    {"range": [70, 100]}
                ]
            }
        )
    )

    fig.update_layout(
        height=400,
        template="plotly_white"
    )

    return fig