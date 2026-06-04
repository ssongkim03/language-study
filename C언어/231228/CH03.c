// (자료)형 변환

// 자동형변환(암시적형변환) :컴파일러에 의해 자동형변환 (컴파일러 : 컴퓨터, 운영체제)
// 강제형변환(명시적형변환) : 프로그래머에 의한 강제 형 변환

// 01) 자동형변환
// 자료형 변환시 데이터 손실가능성이 낮을때 컴파일러(C언어 프로그램)에 의해 자동으로 형변환이 된다. ex) 큰공간 = 작은값

// 자동형변환 순서
// char < short < int < long < long long < float < double

//#include <stdio.h>

//int main()
//{
//	short svar = 10;
//	int ivar = svar; // 자동형변환(큰공간 == 작은값)
//	printf("ivar = %d\n", ivar);
//
//	char cvar = 'a';
//	ivar = cvar; //자동형변환
//	printf("ivar = %d\n", ivar);
//
//	long long lvar = ivar; // 자동형변환
//	printf("ivar = %d\n", ivar);
//
//	float fvar = ivar; // (주의)자동형변환
//	printf("ivar =%d\n", ivar);
//
//	double dvar = ivar; // (주의)자동형변환
//	printf("dvar =%d\n", dvar);
//}

// 02) 강제형변환
// 프로그래머에 의해 특정한 자료형으로 강제 형변환 하는 경우

//#include <stdio.h>
//int main()
//{
//	// int : 약 21, short : 32000
//	int ivar = 50000;
//	short svar = (short)ivar;
//	char cvar = (char)ivar;
//
//	printf("svar = %d\n", svar);
//	printf("cvar = %d\n", cvar);
//}

// 03) 연산시 자동(강제) 형변환(나눗셈)

//#include <stdio.h>
//int main()
//{
//	int num = 10;
//	int div = 4;
//	double r1 = num / div;
//	double r2 = (float)num / div;
//
//	printf("r1 = %f\n", r1);
//	printf("r2 = %f\n", r2);
//}

