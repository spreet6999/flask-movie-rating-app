import plotly.graph_objects as go
import plotly.io as pio

# annotation_text = "CONFIDENTIAL"
annotation_text = None


def set_annotations(annotation_text=None):
    if annotation_text is None:
        annotation = []
    else:
        annotation = [
            go.layout.Annotation(
                name="draft watermark",
                text=annotation_text,
                textangle=-30,
                opacity=0.1,
                font=dict(color="black", size=100),
                xref="paper",
                yref="paper",
                x=0.5,
                y=0.5,
                showarrow=False,
            )
        ]
    return annotation


pio.templates["mck_new"] = go.layout.Template(
    layout_annotations=set_annotations(annotation_text),
    layout=go.Layout(title_font=dict(family="Georgia", size=24),
                     font=dict(family="Georgia", size=14)
                     )
)
