# SMA 2022 SUMMER PROJECT 연구주제 신청서

## 1.데이터 수집 사이트: <br>
국내 개발자 커뮤니티 OKKY
<br><br>

## 2.분석주제: 
*‘동시 출현 네트워크 분석 및 토픽 모델링을 활용한 국내 개발 취업 준비생과 현업자의 경험과 고충 분석: 온라인 커뮤니티 게시글을 중심으로.’*
<br><br>
코로나 사태로 기업들의 내부 디지털 역량 강화 및 디지털 전환 요구가 가속화되며 근 몇 년, 국내 산업계는 IT인력 충원을 위해 개발 인력 확보에 총력을 다하는 모습이 연출되었다. 기업과 중앙 및 각 지자체 등은 산업의 요구와 인력 수요에 발맞춰 K-Digital Training 혹은 그와 유사한 부트캠프 등을 통해 다방면으로 IT 인재육성에 만전을 기하고 있다. 국내 언론은 앞다투어 IT 산업의 대우를 일면에 내걸며 IT업계로의 인력 진입을 다소 무책임하게 과열시켜왔다. 현재 금리인상이 지속되는 냉혹한 현실에서 스타트업 및 IT서비스 업계에 대한 평가와 투자거품은 차갑고 빠르게 꺼지고 있지만 장밋빛 미래를 꿈꾸는 수많은 청년들이 취업에 당면하거나 필드에 나가 마주할 현실을 일러줄 객관적 자료가 터무니없이 부족하다. 본 연구는 국내 취준생 혹은 개발자들이 이용하는 일개의 온라인 커뮤니티 게시글에서 추출한 텍스트를 기반으로 ‘동시 출현 네트워크’와 ‘토픽 모델’을 구성하여 취준생과 현업자들의 경험과 고충을 탐색하는 계량적 내용 분석 연구가 될 것이다. 해당 연구 결과는 IT업계의 취준 및 현업의 현실을 알리는 다소 객관적인 근거자료가 될 수 있으며, 실제 개발업계의 취업준비생과 현업자들의 고충을 반영해야 할 기업의 사내문화 개선 담당자 혹은 각 정부의 정책 담당자를 위한 새로운 아이디어와 정책 근거를 마련할 수 있을 것으로 기대한다. 
<br><br>


## 3.수집 데이터 내용
수집 데이터는 국내에서 활성화된 개발자 커뮤니티인 ‘OKKY’의 ‘사는얘기’(https://okky.kr/articles/life) 탭의 게시물 중 약 6개월-2년 사이의 제목, 내용이 될 것입니다.
<br><br>

## 4.데이터 수집 방법(계획)
OKKY는 공식 API를 지원하지 않기 때문에 Python의 Selenium, BeautifulSoup을 사용해 웹 스크래핑을 이용한 텍스트 데이터 추출을 진행할 것입니다. 현재 25일 기준으로 OKKY 운영팀에게 협조 메일을 보냈으며 추후 불허 응답 시, 허락해주신다면 연구 사이트 재선정 혹은 주제를 빠르게 수정하여 연구에 임하도록 하겠습니다. 연구윤리를 고려하여 개인 게시자를 식별할 수 있는 id, 이름, 관련 내용은 수집하지 않고 수집 이후 적절한 검토를 거쳐 확인 시 삭제할 예정입니다.
<br><br>
## 5.데이터 분석 방법(계획)
수집된 텍스트 데이터는 토큰화와하여 명사만을 추출하여 이후, ‘다빈도 키워드 추출’, ‘동시출현 네트워크 분석’, 그리고 ‘토픽 모델링 텍스트 마이닝 기법’을 적용하는 분석을 진행할 예정입니다.
