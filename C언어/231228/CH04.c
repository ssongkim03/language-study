// 01) 정수값 받기

#include <stdio.h>
//int main()
//{
//	int n1 = 0;
//	printf("정수 1 입력 : ");
//	scanf_s("%d", &n1);
//	// scanf_s : 표준입력장치(키보드)로부터 프로그램 방향으로 값을 받을 때 사용
//	// "%d" : 정수서식에 맞게 값을 받겠다.
//	// &(참조연산자) : 공간의 주소값을 반환
//	printf("입력한 값 : %d\n", n1);
//}

//int main()
//{
//	int n1 = 0;
//	int n2 = 0;
//	printf("정수 2개 입력 : ");
//	scanf_s("%d%d", &n1, &n2); // 값을 스페이스바 혹은 엔터키를 기준으로 확인
//	printf("n1 = %d, n2 = %d\n", n1, n2);
//}

//// 문제
// 정수 3개를 한번에 받아서 세수의 합 / 곱 / 차를 출력해 보세요.

//int main()
//{
//	int n1 = 0;
//	int n2 = 0;
//	int n3 = 0;
//	printf("정수 3개 입력 : ");
//	scanf_s("%d%d%d", &n1, &n2, &n3);
//	printf("세수의 합 = %d\n", n1+n2+n3);
//	printf("세수의 곱 = %d\n", n1*n2*n3);
//	printf("세수의 차 = %d\n", n1-n2-n3);
//
//}

// 03) scanf_s 서식문자 따른 값 받기

// %d : 10진 정수
// %f : 실수(float)형
// %lf : double형 서식
// %c : 문자 서식
// %s : 문자열 서식

//int main()
//{
//	int n1;
//	double n2;
//	char ch;
//
//	printf("정수 입력 : ");
//	scanf_s("%d", n1);
//	printf("저장된 정수 : %d\n", n1);
//
//	printf("실수 입력 : ");
//	scanf_s("%f", &n2);
//	printf("저장된 실수 : %lf\n", n2);
//
//	// scanf를 반복적으로 사용할 때 숫자값 입력과 문자값 입력 사이에 rewind(stdin)을 이용해서 버퍼공간을 초기화시켜주지 않으면 버퍼공간에 남아있는 문자 or 문자열 값이 다음 scanf의 입력된 값으로 해석되기 때문에 문제가 발생한다.
//
//	rewind(stdin);
//
//	printf("문자 입력 : ");
//	scanf_s("%c", &ch);
//	printf("저장된 문자 : %c\n", ch);
//}

// 04) 문자열 받기

//int main()
//{
//	char gender;
//	char name[20];
//
//	printf("성별(M/W) : ");
//	scanf_s("%c", &gender, sizeof(gender));
//	printf("이름 : ");
//	scanf_s("%s", name, sizeof(name));
//
//	printf("이름 : %s\n성별 :% c\n", name, gender);
//}

//// 문제
// 국어, 영어, 수학 점수를 받아 합계와 평균을 출력하세요
// 예
// 국영수 입력 : 100 90 80
// 총점 : 270
// 평균 : 90.0
// 평균점수는 소수점 이하 2자리까지 출력
// 나눗셈 과정에서 소수점이하 값이 유지되도록 강제 형변환 처리


//int main()
//{
//	int 국어;
//	int 영어;
//	int 수학;
//
//	printf("국어, 영어, 수학 점수 : ");
//	scanf_s("%d%d%d", &국어, &영어, &수학);
//	int 총점;
//	총점 = 국어 + 영어 + 수학;
//	printf("총점 : %d\n", 총점);
//	printf("평균 : %.2f\n", (float)총점/3); // .2f 소수점 2번째까지 표시
//
//
//}

//// 문제 2 
// 다음과 같이 출력과 입력을 반복하세요
// 당신의 이름은 무엇입니까? ㅇㅇㅇ
// 박원민 님의 나이는 몇살입니까? 50
// 박원민 님의 나이는 50살입니다

// -> 여기서 홍길동, 40은 고정된 값이 아니라 키보드로 입력값을 받는 변수
// -> 다른 값으로도 바뀔 수 있기 떄문에 두번째 라인에서는 입력받은 이름이
// 출력될 수 있도록 처리


//int main()
//{
//	char name[20];
//	int age;
//
//	printf("당신의 이름은 무엇입니까?");
//	scanf_s("%s", name, sizeof(name));
//	printf("%s 님의 나이는 몇살입니까?", name);
//	scanf_s("%d", &age, sizeof(age));
//	printf("%s님의 나이는 %d살입니다", name, age);
//
//}
