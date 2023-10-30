reference_array = zeros(size(width_array));
for i = 1:length(width_time)
    t = width_time(i);
    if t < 13.1%command_time(1)
        reference_array(i) = 9;
    else
        reference_array(i) = 9;
    end
end

referencef_array = zeros(size(width_f_array));
for i = 1:length(width_f_time)
    t = width_f_time(i);
    if t < 13.1%command_time(1)
        referencef_array(i) = 9;
    else
        referencef_array(i) = 9;
    end
end

figure(1)
subplot(3,1,1)
hold on
grid on
title("Largura do Cordão")
plot(width_time-12.1137, reference_array,'r', 'LineWidth', 4)
axis([0 20 4 10])
%plot(width_time, width_array,'g', 'LineWidth', 2)
plot(width_time-11.8, width_f2_array,'b', 'LineWidth', 4)
axis([0 20 4 10])
%set(gca,'FontSize',18)


xlabel("Tempo [s]")
ylabel("Largura [mm]")
legend("Referência", "Largura")%, "myFilter")

subplot(3,1,2)
hold on
grid on
title("Sinal de Controle")
plot(command_time-12.1137, command_array,'b', 'LineWidth', 4)
axis([0 20 30 70])
xlabel("Tempo [s]")
ylabel("Potência [%]")
%set(gca,'FontSize',18)

subplot(3,1,3)
hold on
grid on
title("Erro")
plot(width_time-12.1137, reference_array - width_f2_array,'r', 'LineWidth', 4)
axis([0 20 -2 5])
%set(gca,'FontSize',18)
xlabel("Tempo [s]")
ylabel("Erro [mm]")
