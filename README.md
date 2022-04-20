# Wanted_pre_onboarding

원티드 프리온보딩 코스 _ Backend 과정 선발과제 ([링크](https://docs.google.com/document/d/1Wu429EZ9tR72ITb5u_5wCfw8s5_U_07a01rWEFZiKyQ/edit))


## 구현 과제
- 상품 등록
	- `제목`, `게시자명`, `상품설명`, `목표금액`, `펀딩종료일`, `1회펀딩금액`으로 구성
- 상품 수정
	- 모든 내용이 수정 가능하나 `목표금액`은 수정불가
- 상품 삭제

- 상품 목록
	- `제목`, `게시자명`, `총펀딩금액`, `달성률`, `D-day`가 포함
	- `달성률` : `총펀딩금액`/`목표금액`*100 (소수점 무시)
	- `D-day` : 펀딩 종료일까지
	- 상품 검색 : 검색된 문자열 포함된 상품 리스트 조회
	- 상품 정렬 : `생성일`, `총펀딩금액` 기준으로 정렬
- 상품 상세
	- `제목`, `게시자명`, `총펀딩금액`, `달성률`, `D-day`, `상품설명`, `목표금액`, `참여자 수`가 포함

## 기술 스택
- Django==4.0.4
- djangorestframework==3.13.1
- sqlite
 

### 상품 등록
POST products/

![product_createapi](https://user-images.githubusercontent.com/86827063/164165763-4c6cc6fb-9f88-44d2-baf4-6c39f73fbe1a.png)

### 상품 목록
GET products/

![product_Listapi](https://user-images.githubusercontent.com/86827063/164165899-eb8639af-764e-4dbe-98c2-2d5ab7191412.png)

### 상품 상세
GET products/<int:pk>/

![product_detail](https://user-images.githubusercontent.com/86827063/164165925-488dcece-2738-4fae-ad93-614e4ea2e72b.png)

### 상품 수정
PUT products/<int:pk>/
![product_Update](https://user-images.githubusercontent.com/86827063/164165919-d54589fa-fbf6-4257-b023-e534a935d834.png)
> 목표 금액이 수정 불가능하므로 read_on_fields 처리

### 상품 삭제
Delete products/<int:pk>/

### 정렬 및 검색
> 정렬<p>
생성순, 총 펀딩금액으로 정렬<p>
![ordering](https://user-images.githubusercontent.com/86827063/164167492-63585a01-5357-4a52-b7dc-a4206969f233.png)

> 검색<p>
제목의 키워드로 검색<p>
![search](https://user-images.githubusercontent.com/86827063/164167516-fab02ca0-c927-4862-adf3-a2c9133371d4.png)
![search2](https://user-images.githubusercontent.com/86827063/164167524-f2271267-7425-4d13-9ac2-1099c3a1511d.png)

<hr>

### 펀딩 생성
POST funding/
![funding_createapi](https://user-images.githubusercontent.com/86827063/164165831-bc4744ea-44dd-4546-87be-fa54fb233120.png)


### 펀딩 목록
GET funding/




### 요구사항 구현
- CBV를 이용하여 작성하면 코드를 간결하게 구현할 수 있을 거라고 생각하여 사용
- 정렬과 검색은 DRF에서 제공하는 django-filter를 이용하여 구현
- Product와 Funding의 모델을 나누어 구현한 이유는 추후에 추가 기능이 생긴다면
    분리하는 것이 나을 것이라고 판단
- Funding이 이루어지면 Product에도 변경이 일어나기 때문에
    ListCreateAPI를 custom 하여 적용

```python
#views.py
class FundingListAPI(generics.ListCreateAPIView):
    queryset = Funding.objects.all()
    serializer_class = FundingListSerializer

    def post(self, request, *args, **kwargs):
        target_product = self.request.data['product']
        product = Product.objects.filter(pk=target_product).get()
        product.total += product.charge
        product.cnt += 1
        product.save()
        return self.create(request, *args, **kwargs)
```
