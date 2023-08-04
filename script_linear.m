n = 0.655;
nd = 0.958;
Ea = 723.2561;
Vo = 5.1782;
Ra = 0.0201;
Rs = 0.004;
Ls = 0.00014;
Voc = 31;
kv = 10; %10, 0.0001
lc = 0.01;
v = 0.12;
DeltaT = 1300;
rho = 0.1319;
k = 24;
alpha = 7.79*10^(-6);
C1 = 3.2634*10^(-10);
C2 = 1.1836*10^(-9);
rw = 0.0006;

lso = 0.0041;
Io = 147.79;
fo = 0.055;
Ir = 146;
weo = 0.0041;
ho = 0.0012;

kw = sqrt((2-nd)/nd);
Aw = pi*rw^2;


Aco = nd*(C2*rho*lso*Io^2 + C1*Io)/v;

Delta = (0.2*2*alpha/(kw*v))^2 - (2*(C2*rho*lso*Io^2 + C1*Io)/(kw^2 + 1) - n*alpha*(Ra*Io + Ea*(lc-lso) + Vo)*Io/(k*DeltaT))/(kw*v);

C11 = ((-2*C2*rho*Io^2)/(kw^2+1) - n*alpha*Ea*Io/(k*DeltaT))/(2*kw*v*sqrt(Delta));

C12 = (-(2*C2*rho*lso*Io + C1)/(kw^2+1) + (n*alpha*(2*Ra*Io + Ea*(lc-lso) + Vo))/(k*DeltaT))/(2*kw*v*sqrt(Delta));

C21 = (nd*C2*rho*Io^2)/v;

C22 = nd*(C1 + 2*C2*rho*lso*Io)/v;

A = [-(C2*rho*Io^2)/Aw, -(C1 + 2*C2*rho*lso*Io)/Aw;
    (Ea - rho*Io)/Ls, -(Ra + Rs + rho*lso + kv)/Ls];

B = [1, 0;
    0, kv/Ls];

C = [C11, C12;
    C21/weo - C11*Aco/weo^2, C22/weo - C12*Aco/weo^2];

D = zeros(2);

Nx = diag([1, 10^4]);
Nu = diag([fo, Ir]);

A_ = inv(Nx) * A * Nx;
B_ = inv(Nx) * B * Nu;
C_ = 1000 * C * Nx;

%theta0 = theta_star;
theta0 = zeros(17,1);
x0 = [0;0];

%% LS-MRAC
gamma = 10; %10 MANTER
R0_mag = 100000; %100000 TUNAR POR AQUI
R0 = R0_mag * eye(17);
lambda = 5; % 5
af = lambda; % 5

%% M-MRAC

gamma_m_mag = 10000;

%% MRAC
gamma_mrac = 1000;

%% LS-MRAC GMAW
input_level = 0.05;
R0_factor = 1/input_level;

% VER GANHO DO CONTROLE DE CORRENTE