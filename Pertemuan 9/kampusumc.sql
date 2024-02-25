-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 05:00 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `joana_deika_pratama`
--

-- --------------------------------------------------------

--
-- Table structure for table `kampusumc`
--

CREATE TABLE `kampusumc` (
  `id` int(11) NOT NULL,
  `kodemk` varchar(100) NOT NULL,
  `namamk` varchar(50) NOT NULL,
  `sks` enum('1','2','3','4','6') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kampusumc`
--

INSERT INTO `kampusumc` (`id`, `kodemk`, `namamk`, `sks`) VALUES
(1, 'KLK22TIF', 'Kalkulus', '2'),
(2, 'AIK2_22TIF', 'Agama Islam dan Kemuhammadiyahan 2', '2'),
(3, 'KMD22TIF', 'Komunikasi Data', '2'),
(4, 'SDP22TIF', 'Statistika dan Probabilitas', '2'),
(5, 'AOK22TIF', 'Arsitektur dan Organisasi Komputer', '2'),
(6, 'PBO22TIF', 'Pemograman Berorientasi II', '3'),
(7, 'SDA22TIF', 'Struktur Data dan Algoritma', '3'),
(8, 'SI22TIF', 'Sistem Informasi', '3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kampusumc`
--
ALTER TABLE `kampusumc`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kampusumc`
--
ALTER TABLE `kampusumc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
