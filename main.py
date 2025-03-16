import pandas as pd
import plotly.express as px


def main():
    df = pd.read_csv('datasets/Top_Anime_data.csv')

    # Заменяем ошибки на NaN
    df['Episodes'] = pd.to_numeric(df['Episodes'], errors='coerce')

    # Удаляем строки с пропусками
    df = df.dropna(subset=['Episodes', 'Anime Score'])

    # Считаем корреляцию
    correlation = df['Anime Score'].corr(df['Episodes'])
    print(f'Корреляция между рейтингом и количеством серий: {correlation}')
    
    fig = px.scatter(
        df, 
        x='Episodes', 
        y='Anime Score', 
        title='Рейтинг vs Количество серий (Интерактивный)',
        labels={'Episodes': 'Количество серий', 'Anime Score': 'Рейтинг'},
        opacity=0.6,
        hover_name='Anime Name' if 'Anime Name' in df.columns else None
    )

    fig.update_traces(marker=dict(size=5))
    fig.update_layout(
        xaxis_title='Количество серий',
        yaxis_title='Рейтинг',
        template='plotly_white'
    )

    fig.show()
    
    
    
if __name__ == "__main__":
    main()