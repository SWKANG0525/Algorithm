/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practice;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

/**
 *
 * @author Kang Ho Dong
 * Date : 2019 - 02 - 01 
 * Title : BOJ 10989 (Counting Sort Algorithm)
 * Link : https://www.acmicpc.net/problem/10989
 * Language : Java 
 * 
 */
public class Practice {

    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     */
    
        // Counting Sort,  Non-Comparison Sort, Time Complexity : O(n)
    
        public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // BufferedReader Instance
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); // BufferedWriter Instance  
        int T = Integer.parseInt(br.readLine()); // Variable T = Test_case;
        int native_dataset[] = new int[T]; // Array native_dataset[], Not sorted Data
        int sorted_dataset[] = new int[T]; // Array sorted_dataset[], Sorted Dataset
        int max_num = 0; // Top of Value in native_dataset
        
        for(int i = 0 ;  i < T; i++) { // Native_dataset Data Input;
            int input = Integer.parseInt(br.readLine());
            if(max_num<input) 
                max_num = input;
            native_dataset[i] = input;    
        }
        
        int cnt_dataset[] = new int[max_num+1]; // Define Count_dataset;
        
        for(int i = 0; i < T; i++) // Input elements count.
            cnt_dataset[native_dataset[i]] += 1;
        
        for(int i = 1; i< max_num+1; i++) // Accumulate elements.
            cnt_dataset[i] += cnt_dataset[i-1];
        
        for(int i = T-1; i>=0; i--) { // Stable Sort.
            cnt_dataset[native_dataset[i]] -= 1;
            sorted_dataset[cnt_dataset[native_dataset[i]]] = native_dataset[i];
        }
        
        for(int i = 0 ; i< T; i++) // Print Elements.
            bw.write(Integer.toString(sorted_dataset[i]) + "\n");
        
        br.close();
        bw.close();
        }
    }

