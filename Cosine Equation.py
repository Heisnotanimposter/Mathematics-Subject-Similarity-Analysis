{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNEYGiedkOizwgjemBCCTJt",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Heisnotanimposter/Strategy-of-Transferring/blob/main/Cosine%20Equation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YPDlRTR75tR4",
        "outputId": "49b280c5-4038-4bb3-c116-5258670b71c0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1.         0.         0.         0.01293174]\n",
            " [0.         1.         0.10509751 0.11051734]\n",
            " [0.         0.10509751 1.         0.07138745]\n",
            " [0.01293174 0.11051734 0.07138745 1.        ]]\n"
          ]
        }
      ],
      "source": [
        "# 세부과목 리스트 정의\n",
        "linear_algebra_topics = [\"벡터\", \"행렬\", \"가우스-요르단 소거법\", \"행 간의 연산\", \"행렬 방정식의 해\", \"행렬 연산자\", \"특정 형태의 행렬\", \"전치\", \"트레이스\", \"역행렬\", \"단위행렬\", \"상부삼각행렬\", \"하부삼각행렬\", \"대칭행렬\", \"LU분해법\", \"선형독립\", \"일차독립\", \"행렬식\", \"고윳값\", \"고유벡터\", \"선형연산자\", \"선형\", \"직교행렬\", \"직교화된 연산\", \"전치행렬\", \"벡터 공간\", \"기저\", \"차원\", \"기본공간\", \"차원 정리\", \"계수정리\", \"피봇정리\", \"영공간\", \"행공간\", \"열공간\", \"벡터의 직교화\", \"그람-슈미트 직교정규화\", \"상사성\", \"대각화\", \"복소수 고윳값\", \"벡터 공간의 공리\"]\n",
        "calculus_diff_topics = [\"함수\", \"집합\", \"원소\", \"대응 규칙\", \"정의역\", \"공역\", \"표현\", \"말로 설명\", \"표\", \"그래프\", \"대수학적 식\", \"극한\", \"x\", \"a\", \"f(x)\", \"L\", \"엡실론-델타 논법\", \"연속\", \"점\", \"제거 가능한 불연속성\", \"미분\", \"변화율\", \"도함수\", \"기울기\", \"상수\", \"합\", \"차\", \"곱\", \"몫\", \"미분 규칙\", \"연쇄법칙\", \"음함수 미분법\", \"삼각함수의 미분\", \"삼각함수\", \"미분 규칙\", \"sinx\", \"cosx\", \"고등학교 수학\", \"대학교\", \"수학 과정\", \"기본적 이해\"]\n",
        "calculus_int_topics = [\"적분\", \"역도함수\", \"부정적분\", \"정적분\", \"구간\", \"연속함수\", \"폭\", \"분할\", \"부분구간\", \"끝점\", \"표본점\", \"정적분의 성질\", \"미적분학의 기본정리\", \"치환 법칙\", \"부분적분법\", \"미분의 곱셈 법칙\", \"넓이\", \"부피\", \"회전체\", \"속도와 거리\", \"속도\", \"거리\", \"좌표평면\", \"곡선의 길이\", \"곡선\", \"부분적분\", \"회전체의 부피\", \"연속\", \"미분 가능\", \"연속 함수\", \"함수\", \"변화량\", \"치역\", \"입체도형\", \"절단면\", \"회전\", \"직선\", \"시각\", \"위치\", \"미분\", \"변형\", \"연속점\", \"불연속점\", \"무한개\", \"실수\", \"상수\", \"임의의 상수\", \"상수배\", \"적분 가능\", \"미분가능\", \"미분의 곱셈 법칙\"]\n",
        "diff_eq_topics = [\"미분 방정식\", \"도함수\", \"함수\", \"변수\", \"함수 방정식\", \"계수\", \"차수\", \"미분 횟수\", \"독립 변수\", \"거듭제곱\", \"응용 수학\", \"매개 변수\", \"의존성\", \"변화율\", \"엔지니어링\", \"물리학\", \"경제학\", \"유체역학\", \"천체역학\", \"순수수학\", \"응용수학\", \"고전역학\", \"뉴턴의 운동 법칙\", \"위치\", \"속도\", \"가속도\", \"힘\", \"운동방정식\", \"중력\", \"공기저항\", \"실세계\", \"수학\", \"해\", \"방정식\", \"컴퓨터\", \"수적 근사값\", \"동역학계 이론\", \"수치 해석 방법\", \"미분 방정식의 목표\", \"상황\", \"미래\", \"예측\", \"전기회로\", \"다리\", \"자동차\", \"비행기\", \"하수도\", \"상미분 방정식\", \"편미분 방정식\", \"선형 미분 방정식\", \"비선형 미분 방정식\", \"나비에-스톡스 방정식\", \"테일러 급수\", \"근사해\", \"제1차 상미분 방정식\", \"1차 제차 상미분 방정식\", \"적분\", \"1차 비제차 상미분 방정식\", \"적분인자\", \"1차 선형 상미분 방정식\"]\n",
        "\n",
        "# 나머지 코드는 그대로 유지\n",
        "from sklearn.feature_extraction.text import TfidfVectorizer\n",
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "\n",
        "# 세부 주제를 문자열로 변환\n",
        "linear_algebra_str = \" \".join(linear_algebra_topics)\n",
        "calculus_diff_str = \" \".join(calculus_diff_topics)\n",
        "calculus_int_str = \" \".join(calculus_int_topics)\n",
        "diff_eq_str = \" \".join(diff_eq_topics)\n",
        "\n",
        "# TF-IDF 벡터화\n",
        "vectorizer = TfidfVectorizer()\n",
        "tfidf_matrix = vectorizer.fit_transform([linear_algebra_str, calculus_diff_str, calculus_int_str, diff_eq_str])\n",
        "\n",
        "# 코사인 유사도 계산\n",
        "cos_sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)\n",
        "\n",
        "# 결과 출력\n",
        "print(cos_sim_matrix)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Ez3bUlQM8zVr"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}