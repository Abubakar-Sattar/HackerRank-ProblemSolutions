package com.javaaid.hackerrank.solutions.languages.java.introduction;

import java.time.LocalDate;
import java.util.Scanner;

public class JavaDateAndTime {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int month = in.nextInt();
		int day = in.nextInt();
		int year = in.nextInt();
		LocalDate dt = LocalDate.of(year, month, day);
		System.out.println(dt.getDayOfWeek());
		in.close();
	}
}
