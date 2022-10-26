
import pandas as pd
import sys
import math



#print(ipf('M','Raw','SBD',73.5,724.5))
IPF_COEFFICIENTS1 = {
    'M': {
        'Raw': {
            'SBD': [1199.72839, 1025.18162, 0.009210],
            'B': [320.98041, 281.40258, 0.01008]
        },
        'Single-ply': {
            'SBD': [1236.25115, 1449.21864, 0.01644],
            'B': [381.22073, 733.79378, 0.02398]
        }
    },
    'F': {
        'Raw': {
            'SBD': [610.32796, 1045.59282, 0.03048],
            'B': [142.40398, 442.52671, 0.04724]
        },
        'Single-ply': {
            'SBD': [758.63878, 949.31382, 0.02435],
            'B': [221.82209, 357.00377, 0.02937]
        }
    }
}


#def goodlift(sex, equipment, event, bodyweight,total):
def ipf1(sex, equipment, event, bodyweightKg, totalKg):
    global IPF_COEFFICIENTS1

    # The IPF set lower bounds beyond which points are undefined.
    if bodyweightKg < 40 or totalKg <= 0:
        return 0

    # Normalize equipment to (Raw, Single-ply).
    if equipment == 'Wraps' or equipment == 'Straps':
        equipment = 'Raw'
    elif equipment == 'Multi-ply':
        equipment = 'Single-ply'

    # The IPF formula is only defined for some parameters.
    if equipment not in ['Raw', 'Single-ply']:
        return 0
    if event not in ['SBD', 'S', 'B', 'D']:
        return 0
    if sex not in ['M', 'F']:
        return 0    
    # Look up parameters.
    [a, b, c] = IPF_COEFFICIENTS1[sex][equipment][event]

    # Calculate the properties of the normal distribution.
    bwt = bodyweightKg
    p = totalKg
    e_pow = math.exp(-1.0 * c * bwt)
    denominator = a - (b * e_pow)

    return (p*(100/denominator))
   

a = 610.32796
b = 1045.59282
c = 0.03048
#e = 
bwt = 75.7
p = 440
e_pow = math.exp(-c * bwt)
#print(e_pow)

#print(a - b * e **(-c*bwt))
denominator = a - (b * e_pow)
print(p*(100/denominator))
b = round(p*(100/denominator),3)
print(b)
#print(p*(100/a-(b*)))
#385 @75.1
#print(ipf1('M','Raw','SBD',73.5,742.5))

#print(round(ipf1('F','Raw','SBD',70.5,452.5),2))
#print(round(ipf1('F','Raw','SBD',70.2,440),3)).
#print(round(ipf1('F','Raw','SBD',70.2,440),3))
#print(ipf1('F','Raw','SBD',70.2,440))

#s = a - (b * e **(-c*bwt)
#print(p*(100/denominator))


# ) -> Points {
#     // Look up parameters.
#     let (a, b, c) = parameters(sex, equipment, event);

#     // Exit early for undefined cases.
#     if a == 0.0 || bodyweight < WeightKg::from_i32(35) || total.is_zero() {
#         return Points::from_i32(0);
#     }

#     // A - B * e^(-C * Bwt).
#     let e_pow = (-1.0 * c * f64::from(bodyweight)).exp();
#     let denominator = a - (b * e_pow);

#     // Prevent division by zero.
#     if denominator == 0.0 {
#         return Points::from_i32(0);
#     }

#     // Calculate GOODLIFT points.
#     // We add the requirement that the value be non-negative.
#     let points: f64 = f64::from(total) * (0.0_f64).max(100.0 / denominator);
#     Points::from(points)
# }

# #[cfg(test)]
# mod tests {
#     use super::*;

#     #[test]
#     fn published_examples() {
#         // Dmitry Inzarkin from 2019 IPF World Open Men's Championships.
#         let weight = WeightKg::from_f32(92.04);
#         let total = WeightKg::from_f32(1035.0);
#         assert_eq!(
#             goodlift(Sex::M, Equipment::Single, Event::sbd(), weight, total),
#             Points::from(112.85)
#         );

#         // Susanna Torronen from 2019 World Open Classic Bench Press Championships.
#         let weight = WeightKg::from_f32(70.50);
#         let total = WeightKg::from_f32(122.5);
#         assert_eq!(
#             goodlift(Sex::F, Equipment::Raw, Event::b(), weight, total),
#             Points::from(96.78)
#         );
#     }
# }
