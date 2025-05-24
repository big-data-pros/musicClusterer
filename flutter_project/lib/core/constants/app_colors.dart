import 'package:flutter/material.dart';

class AppColors {
  // -------------------- Primary Theme Colors -------------------- //
  static const Color primaryColor = Color(0xFFE93989); // electricPink
  static const Color secondaryColor = Color(0xFF3E80B1); // cyanBlue
  static const Color accentColor = Color(0xFFCA1CB0); // neonMagenta

  // -------------------- Background Colors -------------------- //
  static const Color backgroundDark = Color(0xFF1B1B1B); // darkCharcoal
  static const Color backgroundDarker = Color(0xFF1E1E2A); // midnightNavy
  static const Color backgroundLight = Color(0xFFF7D7C7); // palePeach

  // -------------------- Border / Divider / Misc -------------------- //
  static const Color borderColor = Color(0xFF5E6E78); // steelGrey
  static const Color disabledColor = Color(0xFFA04C4F); // mutedRed
  static const Color cardColor = Color(0xFF4C2A58); // deepPurple
  static const Color shadowColor = Color(0xFF202020); // softBlack

  // -------------------- Additional Styling -------------------- //
  static const Color hoverColor = Color(0xFFD2B1E2); // softLavender
  static const Color highlightColor =
      Color(0xFFE93989); // electricPink (reused as highlight)

  // Optional:
  static const Color errorColor = Colors.redAccent;
  static const Color successColor = Colors.greenAccent;

  // -------------------- Primary Text Colors -------------------- //
  static const Color textPrimaryColor =
      Color(0xFFF7D7C7); // Light peach text on dark backgrounds
  static const Color textPrimaryDark =
      Color(0xFF1B1B1B); // Dark text on light backgrounds

  // -------------------- Secondary Text Colors -------------------- //
  static const Color textSecondaryColor = Color(0xFFD2B1E2); // Soft lavender
  static const Color textTertiaryColor =
      Color(0xFFA391B4); // Desaturated purple/grey

  // -------------------- Muted / Disabled Text -------------------- //
  static const Color textMuted =
      Color(0xFF8B7D7C); // Warm grey for hints, subtitles
  static const Color textDisabled =
      Color(0xFF5E6E78); // Steel grey for inactive text

  // -------------------- Alert / Highlight -------------------- //
  static const Color textError =
      Color(0xFFE93989); // Electric pink/red for warnings or emphasis
  static const Color textLink =
      Color(0xFF3E80B1); // Cyan blue for links or actions

  // -------------------- Special Use -------------------- //
  static const Color textInverse =
      Color(0xFF1E1E2A); // For text on bright backgrounds (used on pale peach)
  static const Color textOnPurpleCard =
      Color(0xFFF7F7F7); // Near white for deep purple cards
}