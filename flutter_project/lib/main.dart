import 'package:flutter/material.dart';
import 'package:flutter_project/core/constants/app_colors.dart';
import 'package:flutter_project/features%20/likes/presentation/pages/likes_page.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Music App',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          scaffoldBackgroundColor: AppColors.backgroundDark,
          primaryColor: AppColors.primaryColor,
          dividerColor: AppColors.borderColor,
          cardColor: AppColors.cardColor,
          shadowColor: AppColors.shadowColor,
          iconTheme: const IconThemeData(color: AppColors.textPrimaryColor),
          textTheme: const TextTheme(
            bodyLarge: TextStyle(color: AppColors.textPrimaryColor),
            bodyMedium: TextStyle(color: AppColors.textPrimaryColor),
            titleMedium: TextStyle(color: AppColors.textSecondaryColor),
          ),
          appBarTheme: const AppBarTheme(
            backgroundColor: AppColors.backgroundDarker,
            foregroundColor: AppColors.textPrimaryColor,
            elevation: 0,
          ),
          useMaterial3: true,
        ),
        home: Scaffold(body: LikesPage()));
  }
}
