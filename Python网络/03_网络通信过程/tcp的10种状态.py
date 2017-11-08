#coding=utf-8
#10种状态包括tcp client 和 tcp server 通信中的10种状态

#三次握手的4种状态变化
#1.client 发送syn请求 client 变为syn_sent。

#2.server 接收到 client 发送的syn请求 从listen状态变成syn_recv状态 并发送syn+ack 请求给 client 

#3.client 接收到server 发送的 syn+ack 请求 变成established状态 并发送ack 请求给server

#4.server 接收到 client 发送的ack 请求 变成 established 状态


#三次握手建立后 双方都是established状态发送数据


#四次挥手的6种状态变化
#1.client接收到数据后 按照实际需要 close socket  发送fin请求 client 从established状态变成 fin_wait1 状态

#2.server 接收到 client 发出的fin 请求 从established状态变成close_wait 状态  并发送ack请求给client

 
#3.client 接收到server 的ack请求 变成fin_wait2状态 


#4.当server 最终也调用close 之后 状态变为last_ack 状态 并且给client 发送fin 请求 client 从fin_wait2 变成 time_wait 状态

#5.client 变成 time_wait 状态之后 给server 发出ack 请求 server 接收到 ack 请求后状态从 last_ack 变成close状态

#6.client过段时间后从 time_wait状态 变成 close 状态







